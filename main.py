import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv


load_dotenv()

token = os.getenv('TOKEN')

bot = Bot(token=token)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    # await message.answer(f'Привет!\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}')
    await message.reply(f'Привет!\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}')

@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')

@dp.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(
        photo='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Flag_of_Muscat.svg/1200px-Flag_of_Muscat.svg.png',
        caption='Подпись к изображению'
    )


@dp.message(F.text == 'Как дела?')
async def how_are_you(message:Message):
    await message.answer('OK!')

@dp.message(F.photo)
async def received_photo(message: Message):
    await message.answer(f'ID Photo: {message.photo[-1].file_id}')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())