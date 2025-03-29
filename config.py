import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7890079753:AAEA_Dy9VbmUK3KTnrw5baEwirQFloaq04I")
    API_ID = int(os.environ.get("API_ID", 27886943))
    API_HASH = os.environ.get("API_HASH", "b28d0dae5a57f767716f1d8865560fee")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6586191138")
