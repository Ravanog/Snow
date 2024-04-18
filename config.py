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
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/TG_UPDATES1>CLICK HERE</a> 
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/KUSHALHK>CLICK HERE</a>
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

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @TG_UPDATES1" -metadata author="@TG_UPDATES1" -metadata:s:s title="Subtitled By :- @TG_LINKS_CHANNEL1" -metadata:s:a title="By :- @TG_LINKS_CHANNEL1" -metadata:s:v title="By:- @TG_UPDATES1" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ.
"""

    PROGRESS_BAR = """<b>\n
<blockquote>📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ....</blockquote>

╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ 

<a href=https://t.me/TG_UPDATES1>ʜᴋ ᴘʀᴏᴅᴜᴄᴛɪᴏɴꜱ</a>
</b>"""

    SETTINGS_TXT = """<b>
ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ꜱᴇᴛᴜᴘ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢs: </b>"""

    CAP_TXT = """<b>
<u>📑 Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u>

ᴏᴋᴇʏ,
ꜱᴇɴᴅ ᴍᴇ ʏᴏᴜʀ ᴄᴀᴩᴛɪᴏɴ
ɢᴏ ᴛᴏ ʜᴇʟᴩ ᴍᴇɴᴜᴇ ᴛᴏ ᴄʜᴇᴄᴋ ᴩᴀʀꜱᴇ_ᴍᴏᴅᴇ ᴇxᴀᴍᴩʟᴇꜱ

ᴇɢ:- 

<b>{filename}</b>

File Size: <b>{file_size}</b>

Join us :- @TG_UPDATES1 </b>"""

    THUMBNAIL_TXT = """<b>
 /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
 /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ
</b>"""
  
    EXTRA_TXT = """<b>
    Exᴛʀᴀ Mᴏᴅᴜʟᴇs
ɴᴏᴛᴇ:
ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ꜰᴇᴀᴛᴜʀᴇꜱ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ

𝙲𝙻𝙸𝙲𝙺 𝙱𝙴𝙻𝙾𝚆 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝙰𝙽𝙳 𝚄𝚂𝙴 𝙴𝚇𝚃𝚁𝙰 𝙼𝙾𝙳𝚂... 
𝚂𝚃𝙰𝚈 𝚆𝙸𝚃𝙷 𝚄𝚂 𝙰𝙽𝙳 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝚃𝙾 𝙱𝚁𝙸𝙽𝙶 𝙼𝙾𝚁𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂 𝚁𝙴𝙶𝙰𝚁𝙳𝙸𝙽𝙶 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙱𝙾𝚃𝚂 🥰
</b>"""

    MAHAAN_TXT = """<b>
𝙷𝙴𝚁𝙴 𝚈𝙾𝚄 𝙲𝙰𝙽 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚂𝙾𝙼𝙴 𝚂𝙾𝙽𝙶𝚂 𝙾𝙵 𝚈𝙾𝚄𝚃𝚄𝙱𝙴. 
𝙹𝚄𝚂𝚃 𝚈𝙾𝚄 𝙽𝙴𝙴𝙳 𝚃𝙾 𝚂𝙴𝙽𝙳 𝙰 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙾 𝙼𝙴 /𝚜𝚘𝚗𝚐

𝙴𝚇𝙰𝙼𝙿𝙻𝙴 :- /𝚜𝚘𝚗𝚐 𝚏𝚊𝚍𝚎𝚍

𝙲𝚁𝙴𝙳𝙸𝚃𝚂 @TG_UPDATED1

𝚃𝙷𝙰𝙽𝙺 𝚈𝙾𝚄 🫶</b>"""
