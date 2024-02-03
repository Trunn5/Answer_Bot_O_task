from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import config
import google_sheets.sheets
from bot import keyboards, loader
from bot.loader import dp


@dp.message(Command('admin'))
async def admin(m: types.Message, state: FSMContext):
    await state.clear()
    await m.answer(f"""Привет, Админ👋
Вот ссылка на таблицу https://docs.google.com/spreadsheets/d/{config.SHEET_ID}""", reply_markup=keyboards.update_data_keyboard)


@dp.callback_query(F.data == "update_data")
async def update_data(q: types.CallbackQuery):
    """
    Данные для формировании меню тянуться из гугл таблицы
    """
    await q.answer("Начинается обновление данных")
    # Обновление sheet_data в loader
    loader.change_sheet_data(await google_sheets.sheets.get_data())

    print(loader.sheet_data)

    await q.message.edit_text("✅ Операция прошла успешно")