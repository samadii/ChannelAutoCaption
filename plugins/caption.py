import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import autocaption
from config import Config
from database.database import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait


@autocaption.on_message(~filters.edited, group=-1)
async def editing(bot, message):
    if (message.chat.type == "private"):
        if ("/set_cap" in message.text) and ((len(message.text.split(' ')) == 2) or (len(message.text.split(' ')) == 1)):
            await message.reply_text("🖊️ 𝐒𝐄𝐓 𝐂𝐀𝐏𝐓𝐈𝐎𝐍 \n\nUse this command to set custom caption for any of your channels.\n\n👉 `/set_cap -1001448973320 My Caption`", quote = True)
        elif ("/set_cap" in message.text) and (len(message.text.split(' ')) != 2) and (len(message.text.split(' ')) != 1):
            caption = message.text.markdown.split(' ', 2)[2]
            channel = message.text.split(' ', 2)[1].replace("-100", "")
            try:
                a = await get_caption(channel)
                b = a.caption
            except:
                await update_caption(channel, caption)
                return await message.reply_text(f"**--Your Caption--:**\n\n{caption}", quote=True)
            await message.reply_text("⚠️\n\nA caption already seted for this channel, you should first use /rmv_cap command to remove the current caption and then try seting new.", quote=True)
           
        if ("/set_btn" in message.text) and ((len(message.text.split(' ')) == 2) or (len(message.text.split(' ')) == 1)):
            await message.reply_text("🖊️ 𝐒𝐄𝐓 BUTTON \n\nUse this command to set button for any of your channels.\nSend a Button name and URL(separated by ' | ').\n\n👉 `/set_btn -1001448973320 Channel | https://t.me/channel`", quote = True)
        elif ("/set_btn" in message.text) and (len(message.text.split(' ')) != 2) and (len(message.text.split(' ')) != 1):
            button = message.text.split(' ', 2)[2]
            channel = message.text.split(' ', 2)[1].replace("-100", "").replace("1", "")
            try:
                a = await get_button(channel)
                b = a.button
            except:
                await update_button(channel, button)
                return await message.reply_text(f"**--Your Button--:**\n\n{button}", quote=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(button.split(' | ')[0], url=f"{button.rsplit(' ', 1)[1]}")]]))
            await message.reply_text("⚠️\n\nA button already seted for this channel, you should first use /rmv_btn command to remove the current button and then try seting new.", quote=True)
           
        if (message.text == "/rmv_cap"):
            await message.reply_text("Use this command to remove the current caption of any of your channels.\n\n👉 `/rmv_cap -1001448973320`", quote = True)
        elif ("/rmv_cap" in message.text) and (len(message.text.split(' ')) != 1):
            channel = message.text.split(' ', 1)[1].replace("-100", "")
            try:
                a = await get_caption(channel)
                b = a.caption
            except:
                return await message.reply_text("Caption not setted yet!", quote=True)     
            await del_caption(channel)
            await message.reply_text("✅The Caption Removed Successfully.", quote=True)

        if (message.text == "/rmv_btn"):
            await message.reply_text("Use this command to remove the current button of any of your channels.\n\n👉 `/rmv_btn -1001448973320`", quote = True)
        elif ("/rmv_btn" in message.text) and (len(message.text.split(' ')) != 1):
            channel = message.text.split(' ', 1)[1].replace("-100", "").replace("1", "")
            try:
                a = await get_button(channel)
                b = a.button
            except:
                return await message.reply_text("Button not setted yet!", quote=True)     
            await del_button(channel)
            await message.reply_text("✅The Button Removed Successfully.", quote=True)

    if (message.chat.type == "channel") and (message.video or message.document or message.audio):
        m = message.video or message.document or message.audio
        try:
            channel = str(message.chat.id).replace('-100', '').replace('1', '')
            btn = await get_button(int(channel))
            button = btn.button
        except:
            button = None
            pass
        try:
            channel = str(message.chat.id).replace('-100', '')
            cap = await get_caption(int(channel))
            if message.audio:
                caption = cap.caption.replace("{filename}", f"{m.file_name}").replace("{artist}", f"{m.performer}").replace("{title}", f"{m.title}").replace("{ext}", f".{m.file_name.rsplit('.', 1)[1]}")
            elif message.video:
                caption = cap.caption.replace("{filename}", f"{m.file_name}").replace("{width}", f"{str(m.width)}").replace("{height}", f"{str(m.height)}").replace("{ext}", f".{m.file_name.rsplit('.', 1)[1]}")
            elif message.document:
                caption = cap.caption.replace("{filename}", f"{m.file_name}").replace("{ext}", f".{m.file_name.rsplit('.', 1)[1]}")
        except:
            caption = None
            pass
       
        if button is not None:
            Url = button.rsplit(' ', 1)[1]
            Name = button.split(' | ')[0]
            if caption is not None:
                try:
                    await bot.edit_message_caption(chat_id = message.chat.id, message_id = message.message_id, caption = caption, parse_mode = "markdown", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(Name, url=f"{Url}")]]))
                except Exception as e:
                    print(e)
            elif caption is None:
                try:
                    await bot.edit_message_caption(chat_id = message.chat.id, message_id = message.message_id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(Name, url=f"{Url}")]]))
                except Exception as e:
                    print(e)
        elif (button is None) and (caption is not None):
            try:
                await bot.edit_message_caption(chat_id = message.chat.id, message_id = message.message_id, caption = caption, parse_mode = "markdown")
            except Exception as e:
                print(e)
