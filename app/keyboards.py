from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


command_start_reply = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Reply Button 1')],
    [KeyboardButton(text='Reply Button 2.1'), KeyboardButton(text='Reply Button 2.2')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню')

command_start_inline =InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='dzen', url='https://dzen.ru')]
])


example_db = ['val_1', 'val_2', 'val_3', 'val_4']

async def reply_db_builder():
    rkb = ReplyKeyboardBuilder()
    for val in example_db:
        rkb.add(KeyboardButton(text=val))
    return rkb.adjust(2).as_markup()            # .adjust(n) - кол-во кнопок в ряду

async def inline_db_builder():
    rkb = InlineKeyboardBuilder()
    for val in example_db:
        rkb.add(InlineKeyboardButton(text=val, url='https://dzen.ru'))
    return rkb.adjust(2).as_markup()




