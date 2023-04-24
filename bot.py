# https://t.me/q325ygyqw67yu23e_bot

import os

from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import cv2

import numpy as np

def fooba() -> int:
    return "Hello World!"

# /start -> 'Hello World!'
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update)
    if update.message:
        await update.message.reply_text('Hello!')

async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update)
    if update.message:
        await update.message.reply_text('Hello World!')
        
async def photo_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update)
    if not update.message:
        return
    message = update.message
    photo = message.photo[-1] # берём фото с лучшим расширением
    photo_file = await photo.get_file() # берём у телеграма метаданные о файле картинки
    photo_data = await photo_file.download_as_bytearray() # скачиваем саму картинку в память в виде bytearray
    
    buf = np.frombuffer(photo_data, dtype=np.uint8) # конвертируем в ndarray
    img = cv2.imdecode(buf, cv2.IMREAD_COLOR) # конвертируем в cv2 image
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # поворачиваем на 90 градусов по часовой стрелке
    
    ok, rotated_bytes = cv2.imencode('.jpg', rotated) # конвертируем в ndarray
    if not ok:
        raise Exception('Failed to encode image')
    
    await message.reply_photo(photo=InputFile(rotated_bytes.tobytes()))
        
            

if __name__ == '__main__':
    token = os.environ['TELEGRAM_TOKEN']
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_message))
    application.add_handler(MessageHandler(filters.PHOTO, photo_message))
    
    application.run_polling()