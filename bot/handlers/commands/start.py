from aiogram import types
from aiogram.filters import Command

from bot.loader import dp


@dp.message(Command('start'))
@dp.message(Command('menu'))
@dp.message(Command('change'))
async def start(m: types.Message):
    await m.answer("""👋 Привет
Добро пожаловать в админ панель, выбери нужный пункт меню⬇️""")
