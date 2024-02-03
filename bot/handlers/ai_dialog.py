from pprint import pprint

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

    # Проверяем ограничения токенов
    history = process_token_limit(history)

    # Ответ ChatGPT
    answer = await chatGpt.api.get_message(history)

    answer = str(answer)

    # Добавляем ответ в историю
    history.append({"role": "assistant", "content": answer})
    await state.update_data({'ai_history': history})

    pprint(history)

    await m.answer(answer, parse_mode=None)


def process_token_limit(messages: list, max_tokens=4096):
    """
    Функция для обработки ограничения на количество токенов
    :param messages: list, вида:
    [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."},
        {"role": "assistant", "content": "Sure, here's a joke: Why did the chicken cross the road? ..."}
    ]
    """
    total_tokens = sum(len(message['content'].split()) for message in messages)
    while total_tokens > max_tokens:
        # Удалить первое сообщение (после системного), чтобы уменьшить общее количество токенов
        removed_tokens = len(messages[1]['content'].split())
        messages.pop(1)
        total_tokens -= removed_tokens

    return messages
