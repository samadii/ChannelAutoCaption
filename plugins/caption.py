import os
from config import Config

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

CAPTION=Config.CAPTION

@Client.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    await message.edit(CAPTION)
