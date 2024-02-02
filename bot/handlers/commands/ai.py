from aiogram import types
from aiogram.filters import Command

from bot.loader import dp


@dp.message(Command('ai'))
async def start(m: types.Message):
    await m.answer("""Привет, Админ👋
Вот ссылка на таблицу {link}""", keyboards=...)
