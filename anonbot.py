import logging
from pyrogram import Client, idle
import Config
from pyrogram.errors import AccessTokenInvalid, ApiIdInvalid, ApiIdPublishedFlood

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

app = Client(
    "Anonymous-Sender-Bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="AnonymousSenderBot"),
)

# Run Bot
if __name__ == "__main__":
    try:
        app.start()  # Not using run as wanna print
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} Started Successfully!")
    idle()
    app.stop()
    print("Bot stopped. Alvida!")