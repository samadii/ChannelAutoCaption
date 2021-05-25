# Infinity Bots

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

@Client.on_message(filters.document & filters.channel)
async def caption(client, message: Message):
    await message.edit("Your caption here",
          reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Button Name", url="https://t.me/JEBotZ")]
            ]
                                           )
                      )
