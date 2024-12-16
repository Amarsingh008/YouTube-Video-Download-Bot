import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7696666754:AAH2TzzicO9hCSI5QK3_yipiiYWggkS6WHQ")
    API_ID = int(os.environ.get("API_ID", "24519654"))
    API_HASH = os.environ.get("API_HASH", "1ccea9c29a420df6a6622383fbd83bcd")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1002036328603")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
