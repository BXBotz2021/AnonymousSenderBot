from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Start Message
@Client.on_message(filters.private & filters.command("start"))
async def start(anonbot, update)
    text = START_TEXT.format(update.from_user.id)
    await update.reply_text(
        text="hey👋 welcome

        bot started bro 😁🙌",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.buttons),
    )
