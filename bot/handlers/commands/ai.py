from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.loader import dp
from bot.states import Ai


@dp.message(Command('ai'))
async def ai_message(m: types.Message, state: FSMContext, prompt: str = ""):
    await state.update_data({'ai_history': [{'role': 'system', 'content': prompt}]})
    await state.set_state(Ai.ai)
    await m.answer("""Напишите сообщение ⬇️""")


@dp.callback_query(F.data == "/ai")
async def ai_callback(q: types.CallbackQuery, state: FSMContext):
    await ai_message(q.message, state)