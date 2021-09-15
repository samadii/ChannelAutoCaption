import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import pyrogram
from pyrogram import filters
from bot import autocaption
from config import Config
from database.database import *
from translation import Translation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
 

start_button=InlineKeyboardMarkup(
        [
              [
                  InlineKeyboardButton("About Markdown", callback_data = "markdown_data"), 
                  InlineKeyboardButton("About Dynamic", callback_data = "dynamic_data")
              ],
              [
                  InlineKeyboardButton("Source Code", url = "https://github.com/samadii/ChannelAutoCaption"),
                  InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
              ]
        ]
)


@autocaption.on_message(filters.command("start") & filters.private)
async def start(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Translation.START_TEXT.format(cmd.from_user.first_name), 
          reply_to_message_id = cmd.message_id,
          parse_mode = "markdown",
          disable_web_page_preview = True, 
          reply_markup = start_button
      )


# call_backs 

@autocaption.on_callback_query()
async def button(bot, cmd: CallbackQuery):
    cb_data = cmd.data
    if "back_data" in cb_data:
          await cmd.message.edit(
               text=Translation.START_TEXT.format(cmd.from_user.first_name),
               parse_mode="markdown", 
               disable_web_page_preview=True, 
               reply_markup=start_button
          )
    elif "close_data" in cb_data:
          await cmd.message.delete()
          await cmd.message.reply_to_message.delete()

    elif "markdown_data" in cb_data:
          await cmd.message.edit(
               text=Translation.MARKDOWN_TEXT,
               parse_mode="html", 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                       [
                        InlineKeyboardButton("⬇️ BACK", callback_data="back_data"),
                        InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                       ]
 
                   ] 
               ) 
          )
    elif "dynamic_data" in cb_data:
          await cmd.message.edit(
               text=Translation.DYNAMIC_TEXT,
               parse_mode="html", 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                       [
                        InlineKeyboardButton("⬇️ BACK", callback_data="back_data"),
                        InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                       ]
 
                   ] 
               ) 
          )
