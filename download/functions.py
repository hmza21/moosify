import os
import logging
from typing import List
from dotenv import load_dotenv
from savify.track import Track
from savify.utils import PathHolder
from moosify.settings import MEDIA_ROOT
from savify import Savify, Quality, Format
from django.core.handlers.wsgi import WSGIRequest

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
    )

    savify.download(url)
    return savify._parse_query(url)

def download_track(url: str):
    return download(url)[0]

def lookup(url: str) -> list:
    
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