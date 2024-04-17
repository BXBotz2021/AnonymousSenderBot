from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(anonbot, msg):
    print("/start")
    await anonbot.send_message(
        msg.chat.id,
        Data.START.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(Data.buttons),
    )
