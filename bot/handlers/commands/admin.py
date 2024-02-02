from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot import keyboards, loader
from bot.loader import dp


@dp.message(Command('admin'))
async def admin(m: types.Message, state: FSMContext):
    await state.clear()
    await m.answer("""Привет, Админ👋
Вот ссылка на таблицу {link}""", reply_markup=keyboards.update_data_keyboard)


@dp.callback_query(F.data == "update_data")
async def update_data(q: types.CallbackQuery):
    """
    Данные для формировании меню тянуться из гугл таблицы
    """
    await q.answer()
    # Обновление sheet_data в loader
    # test mode without google sheets module
    loader.change_sheet_data([["Бренд", "От кого работаете", "Настроение", "Промпт"],
                              ["Мтс", "От агента", "Весело", "123"],
                              ["Мтс", "От бренда", "Весело", "32"],
                              ["Мтс", "От агента", "Грустно", "123213"],
                              ["Билайн", "фыв", "Настроение", "435454"],
                              ])
    print(loader.sheet_data)
    await q.message.edit_text("✅ Операция прошла успешно")