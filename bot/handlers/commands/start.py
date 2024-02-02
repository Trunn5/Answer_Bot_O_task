from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot import keyboards, loader
from bot.loader import dp


@dp.message(Command('start'))
@dp.message(Command('menu'))
@dp.message(Command('change'))
async def start(m: types.Message, state: FSMContext):
    print(loader.sheet_data)
    await state.clear()
    await m.answer("""👋 Привет
Добро пожаловать в админ панель, выбери нужный пункт меню⬇️""", reply_markup=keyboards.parameter_keyboard([]))
