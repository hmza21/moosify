# Moosify

**Moosify** is a Spotify downloader based on [Savify](https://github.com/LaurenceRawlings/savify). For now, access is limited to premade accounts given by the developer.

## To-do

* [ ] Add support for albums and playlists

## Requirements

* Python 3.10.12 or later
* All packages in requirements.txt
* Nothing else!

> NOTE: You will have to manually go to Savify's main class and change the import at the top. This is because `youtube_dl` became deprecated, and `yt_dlp` is a fork of it that works just the same.

```python
# Original
from youtube_dl import YoutubeDL

# Modification
from yt_dlp import YoutubeDL
```

## Post-clone Tasks

1. Create a Django superuser
2. Create .env file and fill it with your `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, `SPOTIPY_REDIRECT_URL`, and `DJANGO_SECRET` (which is usually auto-generated)
3. Apply migrations
4. Manually create allowed user accounts
5. Install `screen` command using your Linux distro's package manager

   ```bash
   sudo apt install screen
   ```

## Running Guide

To start the development server, run `start.py`, no virtual environment or admin privilages needed. To shut down the server and the cleaner, use `screen` to access and detach the the processes.

To access the screens:

```bash
screen -r moosify_dev
screen -r moosify_cleaner
```

To terminate the process, press `Ctrl+C` while on the screen. To exit without terminating, press `Ctrl+A` then `D` on the screen you're on.

> Another note: this is development build, do NOT use in prodution without proper settings!
