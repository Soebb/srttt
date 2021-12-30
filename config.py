import os

class Config:
    if 'BOT_TOKEN' in os.environ:
        BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
        APP_ID = os.environ.get('API_ID', None)
        API_HASH = os.environ.get('API_HASH', None)
    else:
        BOT_TOKEN = ' '
        APP_ID = ' '
        API_HASH = ' '

    ALLOWED_USERS = '1601268629'
    DOWNLOAD_DIR = 'downloads'
