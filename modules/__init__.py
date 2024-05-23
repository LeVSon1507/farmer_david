# modules/__init__.py

from .commands import (
    handle_google_search,
    handle_youtube_search,
    handle_vscode_open,
    handle_weather,
    handle_time,
    handle_news,
    handle_music,
    handle_reminder,
    handle_email,
    handle_facebook,
    handle_job_information,
    handle_random_video,
)
from .utils import speak, welcome, get_command
from .music import play_music
from .news import read_news
from .reminder import set_reminder
from .weather import get_weather
