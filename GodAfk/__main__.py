import importlib
import time
import re
import sys
from termcolor import colored, cprint
from sys import argv
from typing import Optional
from GodAfk import dispatcher, updater, LOGGER
from AWAY import ALL_MODULES
from misc import paginate_modules
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import BadRequest, ChatMigrated, NetworkError, TelegramError, TimedOut, Unauthorized
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler, Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
from misc.chat_status import *
AFKSAY = """—🚸••÷[Gσԃ Aϝƙ Bσƚ]÷••🚸—
ᴡᴀɪᴛ ɪ ʜᴇᴀʀᴅ ᴛʜᴀᴛ ʏᴏᴜ ɴᴇᴇᴅᴇᴅ ꜱᴏᴍᴇᴛʜɪɴɢ ᴛʜᴀᴛ ᴡᴏᴜʟᴅ ꜱᴀʏ ᴛʜᴀᴛ ʏᴏᴜ ᴀʀᴇ ᴀꜰᴋ.
𝘞𝘦𝘭𝘭 𝘸𝘦𝘭𝘭 𝘞𝘦𝘭𝘭, 𝘥𝘰𝘯'𝘵 𝘺𝘰𝘶 𝘸𝘰𝘳𝘳𝘺.

ᴊᴜꜱᴛ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴛʏᴘᴇ /afk ᴀɴᴅ ʀᴇꜱᴛ ɪꜱ ᴍʏ ᴡᴏʀᴋ.


🖥 Dҽʋ Mҽɳƚισɳ: @TeamGodEye
—🚸••÷[ Gσԃ Aϝƙ Bσƚ ]÷••🚸—
"""
GOD_AFK_BOT_IMG = "https://telegra.ph/file/9a94a34230b123a0daf21.jpg"
IMPORTED = {}
HELPABLE = {}
GDPR = []

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("AWAY." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__
    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    if hasattr(imported_module, "__gdpr__"):
        GDPR.append(imported_module)


def start(update: Update, context: CallbackContext):
    if update.effective_chat.type == "private":
        update.effective_message.reply_photo(
            GOD_AFK_BOT_IMG,
            AFKSAY,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    text="••÷  Add AFKBot to group  ÷••",
                    url="t.me/{}?startgroup=true".format(context.bot.username),)], ]),)
    else:
        update.effective_message.reply_photo(
            GOD_AFK_BOT_IMG,
            "—🚸••÷[Gσԃ Aϝƙ Bσƚ]÷••🚸—\n\n♦️𝐈𝐌𝐏𝐎𝐑𝐓𝐀𝐍𝐓♦️\n𝘐 𝘩𝘢𝘷𝘦 𝘵𝘰 𝘣𝘦 𝘢𝘥𝘮𝘪𝘯 𝘪𝘯𝘰𝘳𝘥𝘦𝘳 𝘵𝘰 𝘸𝘰𝘳𝘬 𝘱𝘳𝘰𝘱𝘦𝘳𝘭𝘺.\n\n—🚸••÷[Gσԃ Aϝƙ Bσƚ]÷••🚸—",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    text="••÷   🆅🅸🆂🅸🆃 ☆🍫 ÷••",
                    url="https://t.me/GodEyeSupport")], ]),)


def main():
    start_handler = CommandHandler("start", start, run_async=True)
    dispatcher.add_handler(start_handler)


LOGGER.info("READY")
cprint(f"               —••÷[ Gσԃ Aϝƙ Bσƚ ]÷••—    online", 'yellow')
updater.start_polling(timeout=15, read_latency=4, drop_pending_updates=True)
main()
updater.idle()
cprint(f"—••÷[ Gσԃ Aϝƙ Bσƚ ]÷••—    offline", 'white', 'on_red')
cprint(f"—🖥 Dҽʋ Mҽɳƚισɳ: ", 'red')
cprint(f"@TeamGodEye", 'green')
updater.stop()
