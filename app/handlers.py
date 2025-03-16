from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    # await message.answer(f'Привет!\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}')
    await message.reply(f'Привет!\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}')

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')

@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(
        photo='https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Flag_of_Muscat.svg/1200px-Flag_of_Muscat.svg.png',
        caption='Подпись к изображению'
    )


@router.message(F.text == 'Как дела?')
async def how_are_you(message:Message):
    await message.answer('OK!')

@router.message(F.photo)
async def received_photo(message: Message):
    await message.answer(f'ID Photo: {message.photo[-1].file_id}')