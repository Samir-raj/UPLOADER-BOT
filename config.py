import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = "5830014306:AAGEy_sxm8fpZ_tzvEzn96tsaaY58xgJau8"
    # The Telegram API things
    API_ID = 25117040
    API_HASH = "d1cfa64ebbb012620a69b133a2428c25"
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 4194304000 #2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = 5470140997
    SESSION_NAME = "UPLOADER-X-BOT"
    # database uri (mongodb)
    DATABASE_URL = "mongodb+srv://abhisen2408:abhisen2408@cluster0.ni4var9.mongodb.net/?retryWrites=true&w=majority"
    MAX_RESULTS = "50"
    PREMIUM_USER = "False"
