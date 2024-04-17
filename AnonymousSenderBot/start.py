from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(anonbot, message):
    print("/start")
    await anonbot.send_message(
        message.chat.id,
        Data.START(),
        reply_markup=InlineKeyboardMarkup(Data.buttons),
    )
