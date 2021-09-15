class Translation(object):

      
      START_TEXT = """
😃 Hi {},
I am Channel Auto Caption bot.
I can automatically add pre-setted caption and button to the files.
You can also use Markdown styles, supported Dynamic variables in seting caption (Details in below buttons).
• Commands
- /set_cap To Set Caption
- /set_btn To Set Button
- /rmv_cap To Remove Caption
- /rmv_btn To Remove Button
⚠️NOTE
➪ Before seting, ensure that bot is admin in your channel with editing permission.
"""    
      DYNAMIC_TEXT = """
🔰 <u>About Dynamic</u>
- You can add {variable_name} in caption, bot will replace these variables by its value according to file.
  Example: Title: {filename}
  Supported variables:
  filename, ext
  Additional variables:
  For video files: width, height
  For audio files: title, artist
"""


      MARKDOWN_TEXT = """
🔰 <u>𝐀𝐛𝐨𝐮𝐭 𝐌𝐚𝐫𝐤𝐝𝐨𝐰𝐧</u>
👉 <b>Bold text</b>
      
📌 <code>**text**</code>
👉 <b>Italic text</b>
📌 <code>__text__</code>
👉 <b>Underline text</b>
      
📌 <code>--text--</code>
👉 <b>Strike text</b>
📌 <code>~~text~~</code>
👉 <b>Code text</b>
📌 <code>`text`</code>
👉 <b>Hyperlink text</b>
📌 <code>[text](https://t.me/durov)</code>
"""
