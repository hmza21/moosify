"""
CLEANER.PY is a daemon dedicated to cleaning up tracks
from media/ directory. It will remove tracks that have
exceeded a certain age, or tracks that are not in the
database.
"""

import logging
from os import remove
from time import sleep
from pathlib import Path
from sqlite3 import connect
from datetime import datetime
from pytz import timezone, utc
from moosify.settings import MEDIA_ROOT

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CYCLE_TIME = 10 # time in minutes
tz = timezone('UTC')

# method to delete track from database
def delete_track(track_id: int):
    conn = connect('db.sqlite3')
    cursor = conn.cursor()

    delete_query = f"DELETE FROM download_track WHERE id = {track_id};"
    cursor.execute(delete_query)

    conn.commit()
    conn.close()

# method to fetch all tracks from database
def fetch_tracks() -> tuple:
    conn = connect('db.sqlite3')
    cursor = conn.cursor()

    query = "SELECT * FROM download_track;"
    cursor.execute(query)

    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result

try:
    logger.info("Starting cleaner.py...")
    while True:
        result = fetch_tracks()

        for track in result:
            file = Path(MEDIA_ROOT, f"{track[2]}".replace(":", "□").replace("/", "□"))

            if not file.is_file(): # if file does not exist
                logger.info(f"Deleted: {track[2]}; file does not exist")
                delete_track(track[0])

            else:
                if track[5]: # if track has been downloaded
                    logger.info(f"Deleted: {track[2]}; track has been downloaded")
                    delete_track(track[0])
                    remove(file)

                else:
                    created_at = datetime.strptime(track[3] + " UTC", "%Y-%m-%d %H:%M:%S.%f %Z")
                    hours_since_downloaded = (datetime.now(utc) - tz.localize(created_at)).seconds / 60 / 60

                    if hours_since_downloaded >= 2: # if track has been in the database for more than 2 hours
                        logger.info(f"Deleted: {track[2]}; track has been in the database for more than 2 hours")
                        delete_track(track[0])
                        remove(file)

        sleep(60 * CYCLE_TIME) # delay

except KeyboardInterrupt:
    print("Exiting cleaner.py...")
    exit(0)
