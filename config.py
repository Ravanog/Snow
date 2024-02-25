import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")  # ⚠️ Required

    # premium 4g renaming client
    STRING_API_ID = os.environ.get("STRING_API_ID", "")
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    DB_URL = os.environ.get("DB_URL", "")  # ⚠️ Required

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "")
    ADMIN = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMIN', '').split()]  # ⚠️ Required
    
    FORCE_SUB = os.environ.get("FORCE_SUB", "") # ⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))  # ⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get(
        "BANNED_USERS", "1234567890").split())

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hᴀɪ {} 👋,
    
I Aᴍ Fɪʟᴇ Rᴇɴᴀᴍᴇ Bᴏᴛ Wɪᴛʜ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ & Cᴀᴘᴛɪᴏɴ Sᴜᴘᴘᴏʀᴛ.
Aɴᴅ Rᴇɴᴀᴍᴇ Wɪᴛʜᴏᴜᴛ Dᴏᴡɴʟᴏᴀᴅ 💯 Fᴜʟʟʏ Wᴏʀᴋ Oɴ Tɢ</b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : {}
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/TG_LINKS_CHANNEL2>CLICK HERE</a> 
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/TG_UPDATES1>CLICK HERE</a>
├📕 Lɪʙʀᴀʀy : <a href=https://github.com/Kushalhk>CLICK HERE</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├📊 Bᴜɪʟᴅ Vᴇʀꜱɪᴏɴ: Rᴇɴᴀᴍᴇʀ V3.0.0</a></b>     
╰───────────────⍟ """

    HELP_TXT = """
  <b><u>Hᴏᴡ Cᴀɴ I Hᴇʟᴘ Yᴏᴜ?</b></u>

ɪ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴍᴇᴅɪᴀ ᴡɪᴛʜᴏᴜᴛ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ɪᴛ!
sᴘᴇᴇᴅ ᴅᴇᴘᴇɴᴅs ᴏɴ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ᴅᴄ.

ɪᴜsᴛ sᴇɴᴅ ᴍᴇ ᴍᴇᴅɪᴀ ᴛᴏ ʀᴇɴᴀᴍᴇ
sᴇɴᴅ ɪᴍᴀɢᴇ ᴛᴏ sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ 
ᴛᴏ sᴇᴇ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴘʀᴇss

ℹ️ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/TG_SUPPORT_GROUP>𝑺𝑼𝑷𝑷𝑶𝑹𝑻 𝑮𝑹𝑶𝑼𝑷</a>
"""


    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @TG_LINKS_CHANNEL1" -metadata author="@TG_UPDATES1" -metadata:s:s title="Subtitled By :- @TG_LINKS_CHANNEL1" -metadata:s:a title="By :- @TG_LINKS_CHANNEL1" -metadata:s:v title="By:- @TG_UPDATES1" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ.
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""
