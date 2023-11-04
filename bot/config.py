import os


class Config:

    BOT_TOKEN = "6398068412:AAEVJfNrEuALTsGXmlHWyzOybYVqWzf1cj4"

    SESSION_NAME = "uploadtgtoytbot"

    API_ID = "6740487"

    API_HASH = "802dbc602fc001d0f01f540da73d88c7"

    CLIENT_ID = "450512777651-9osmbssue4vhclvg8emmmbpb7aopm56o.apps.googleusercontent.com"

    CLIENT_SECRET = "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"

    AUTH_USERS = [1098083004]

    VIDEO_DESCRIPTION = "#Movies #FilmLovers #CinemaMagic #MovieNights #Entertainment #MovieReview #MovieBuff #FilmCollection #Blockbusters #ClassicMovies"

    VIDEO_CATEGORY = ""

    VIDEO_TITLE_PREFIX = ""

    VIDEO_TITLE_SUFFIX = "New Movie Latest|HD Bollywood Movie|HD South Movie"

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
