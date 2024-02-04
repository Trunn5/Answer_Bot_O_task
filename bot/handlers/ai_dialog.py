from aiogram import types
from aiogram.fsm.context import FSMContext

import chatGpt
from bot.loader import dp
from bot.states import Ai

@dp.message(Ai.ai)
async def ai(m: types.Message, state: FSMContext):
    """
    Обработчик сообщений в режиме общения с ChatGPT
    """
    history = (await state.get_data())['ai_history'] + [{"role": "user", "content": m.text}]
    await m.bot.send_chat_action(m.chat.id, "TYPING")
    # Ответ ChatGPT
    answer = await chatGpt.api.get_message(history)


    # Добавляем ответ в историю
    history.append({"role": "assistant", "content": answer})
    await state.update_data({'ai_history': history})

    await m.answer(answer, parse_mode=None)

