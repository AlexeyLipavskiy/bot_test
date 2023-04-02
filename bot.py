# https://t.me/q325ygyqw67yu23e_bot

import asyncio
import telegram
import os

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


# /start -> 'Hello World!'
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update)
    await update.message.reply_text('Hello!')

async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update)
    await update.message.reply_text('Hello World!')

if __name__ == '__main__':
    token = os.environ['TELEGRAM_TOKEN']
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_message))
    
    application.run_polling()
