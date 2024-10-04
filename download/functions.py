import os
import logging
from typing import List
from dotenv import load_dotenv
from savify.track import Track
from savify.utils import PathHolder
from moosify.settings import MEDIA_ROOT, BASE_DIR
from savify import Savify, Quality, Format

def download(url: str) -> list:

    load_dotenv()

    logging.basicConfig(level = logging.INFO)
    logger = logging.getLogger(__name__)

    savify = Savify(
        api_credentials = (os.getenv("SPOTIPY_CLIENT_ID"), os.getenv("SPOTIPY_CLIENT_SECRET")),
        quality = Quality.BEST,
        download_format = Format.MP3,
        path_holder = PathHolder(downloads_path = MEDIA_ROOT),
        logger = logger,
        ydl_options = { 'cookiefile': str(BASE_DIR / 'cookies.txt') }
    )

    savify.download(url)
    return savify._parse_query(url)

def download_track(url: str):
    return download(url)[0]

def download_playlist(url: str):
    return download(url)

def lookup_track(url: str) -> Track:
    
    load_dotenv()

    logging.basicConfig(level = logging.INFO)
    logger = logging.getLogger(__name__)

    savify = Savify(
        api_credentials = (os.getenv("SPOTIPY_CLIENT_ID"), os.getenv("SPOTIPY_CLIENT_SECRET")),
        quality = Quality.BEST,
        download_format = Format.MP3,
        path_holder = PathHolder(downloads_path = MEDIA_ROOT),
        logger = logger,
    )
    
    return savify._parse_query(url)[0]

def lookup(url: str) -> List[Track]:
    
    load_dotenv()

    logging.basicConfig(level = logging.INFO)
    logger = logging.getLogger(__name__)

    savify = Savify(
        api_credentials = (os.getenv("SPOTIPY_CLIENT_ID"), os.getenv("SPOTIPY_CLIENT_SECRET")),
        quality = Quality.BEST,
        download_format = Format.MP3,
        path_holder = PathHolder(downloads_path = MEDIA_ROOT),
        logger = logger,
    )
    
    return savify._parse_query(url)