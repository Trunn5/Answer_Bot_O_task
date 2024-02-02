from aiogram import types, F
from aiogram.filters import Command

from bot.loader import dp


@dp.message(Command('admin'))
async def admin(m: types.Message):
    await m.answer("""Привет, Админ👋
Вот ссылка на таблицу {link}""", keyboards=...)


@dp.callback_query(F.text == "update_data")
async def update_data(q: types.CallbackQuery):
    """
    Данные для формировании меню тянуться из гугл таблицы
    :param q:
    :return:
    """
    await q.answer()
    ...
    await q.message.answer("✅ Операция прошла успешно")