from os import environ 

class Config:
    API_ID = environ.get("API_ID", "24262622")
    API_HASH = environ.get("API_HASH", "50831eb3329ed9c0557aa2bc6aa34376")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6260622606:AAF6CzWlP0mrHpcqZZsEMhi-rNyXQLQ5SKs") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1477222048').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
