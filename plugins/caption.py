import os
from config import Config

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

CAPTION=Config.CAPTION


@Client.on_message(filters.channel & filters.media)
async def caption(client, message: Message):
    button_name = os.environ.get('BUTTON_NAME')
    button_url = os.environ.get('BUTTON_URL')
    FILE_NAME = bool(os.environ.get('FILE_NAME', False))
    if FILE_NAME and not button_name:
        media = message.audio or message.video or message.document or message.animation
        if (media is not None) and (media.file_name is not None):
            file = media.file_name
            _file = file.replace("-", " ").replace("_", " ").replace(".mp4", " ").replace(".mkv", " ").replace(".pdf", " ").replace(".apk", " ").replace(".mp3", " ").replace(".zip", " ")
            caption = CAPTION
            await message.edit(
                f"{_file}\n\n"
                f"{caption}")
        else:
            await message.edit(CAPTION)
    if FILE_NAME and button_name: 
        media = message.audio or message.video or message.document or message.animation
        if (media is not None) and (media.file_name is not None):
            file = media.file_name
            _file = file.replace("-", " ").replace("_", " ").replace(".mp4", " ").replace(".mkv", " ").replace(".pdf", " ").replace(".apk", " ").replace(".mp3", " ").replace(".zip", " ")
            caption = CAPTION
            await message.edit(
                f"{_file}\n\n"
                f"{caption}",
                  reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(button_name, url=f"{button_url}")]
                ]
                                               )
                          )
        else:
            await message.edit(CAPTION,
                  reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(button_name, url=f"{button_url}")]
                ]
                                               )
                          )
    if button_name and not FILE_NAME:
        await message.edit(CAPTION,
              reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(button_name, url=f"{button_url}")]
            ]
                                           )
                      )
    if not button_name and not FILE_NAME:
        await message.edit(CAPTION)
