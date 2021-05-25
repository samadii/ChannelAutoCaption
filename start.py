

from pyrogram import Client, filters

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
  await message.reply("Hey there, I'm channel caption bot. \n\nSource code => https://github.com/samadii/ChannelAutoCaption")
