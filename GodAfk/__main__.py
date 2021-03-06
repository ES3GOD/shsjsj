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
AFKSAY = """âð¸â¢â¢Ã·[GÏÔ AÏÆ BÏÆ]Ã·â¢â¢ð¸â
á´¡á´Éªá´ Éª Êá´á´Êá´ á´Êá´á´ Êá´á´ É´á´á´á´á´á´ ê±á´á´á´á´ÊÉªÉ´É¢ á´Êá´á´ á´¡á´á´Êá´ ê±á´Ê á´Êá´á´ Êá´á´ á´Êá´ á´ê°á´.
ðð¦ð­ð­ ð¸ð¦ð­ð­ ðð¦ð­ð­, ð¥ð°ð¯'ðµ ðºð°ð¶ ð¸ð°ð³ð³ðº.

á´á´ê±á´ á´á´á´ á´á´ ÉªÉ´ Êá´á´Ê É¢Êá´á´á´ á´É´á´ á´Êá´á´ /afk á´É´á´ Êá´ê±á´ Éªê± á´Ê á´¡á´Êá´.


ð¥ DÒ½Ê MÒ½É³ÆÎ¹ÏÉ³: @TeamGodEye
âð¸â¢â¢Ã·[ GÏÔ AÏÆ BÏÆ ]Ã·â¢â¢ð¸â
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
                    text="â¢â¢Ã·  Add AFKBot to group  Ã·â¢â¢",
                    url="t.me/{}?startgroup=true".format(context.bot.username),)], ]),)
    else:
        update.effective_message.reply_photo(
            GOD_AFK_BOT_IMG,
            "âð¸â¢â¢Ã·[GÏÔ AÏÆ BÏÆ]Ã·â¢â¢ð¸â\n\nâ¦ï¸ðððððððððâ¦ï¸\nð ð©ð¢ð·ð¦ ðµð° ð£ð¦ ð¢ð¥ð®ðªð¯ ðªð¯ð°ð³ð¥ð¦ð³ ðµð° ð¸ð°ð³ð¬ ð±ð³ð°ð±ð¦ð³ð­ðº.\n\nâð¸â¢â¢Ã·[GÏÔ AÏÆ BÏÆ]Ã·â¢â¢ð¸â",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    text="â¢â¢Ã·   ðð¸ðð¸ð âð« Ã·â¢â¢",
                    url="https://t.me/GodEyeSupport")], ]),)


def main():
    start_handler = CommandHandler("start", start, run_async=True)
    dispatcher.add_handler(start_handler)


LOGGER.info("READY")
cprint(f"               ââ¢â¢Ã·[ GÏÔ AÏÆ BÏÆ ]Ã·â¢â¢â    online", 'yellow')
updater.start_polling(timeout=15, read_latency=4, drop_pending_updates=True)
main()
updater.idle()
cprint(f"ââ¢â¢Ã·[ GÏÔ AÏÆ BÏÆ ]Ã·â¢â¢â    offline", 'white', 'on_red')
cprint(f"âð¥ DÒ½Ê MÒ½É³ÆÎ¹ÏÉ³: ", 'red')
cprint(f"@TeamGodEye", 'green')
updater.stop()
