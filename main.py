import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6425604599:AAH1BpzGrisvHSeBH-1zy5DLY0CgeedpJWg'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Mening Wikipediya botimga hush kelibsiz :)")

@dp.message_handler()
async def echo(message: types.Message):
    if(message.text == "Assalamu alaikum"):
       await message.answer("Va alaikum Assalam\nIsmingizni kiriting\nMisol: Irodabonu_name")
    if ("name" in message.text):
       await message.answer("Yoshingizni kiriting:\nMisol : 12 yosh")
    if ("yosh" in message.text):
       await message.answer("Ish bo'yicha holatingizni kiriting\nIshlayman | Ishdan bo'shaganman | Ish izlayabman")
    else:
        await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)