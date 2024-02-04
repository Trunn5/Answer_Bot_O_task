import asyncio
from functools import partial

from openai import OpenAI

import config

client = OpenAI(api_key=config.OPENAI_API_KEY)


async def get_message(messages: list) -> str:
    """
    Выполняет запрос к chatGPT
    Raises:
        Переполнение токенов
    :param messages: история сообщений + текущий prompt
    :return: Строка с ответом
    """
    loop = asyncio.get_event_loop()
    while True:
        try:
            partial_api_request = partial(client.chat.completions.create, model="gpt-3.5-turbo", messages=messages)
            res = await loop.run_in_executor(
                None,
                lambda: partial_api_request()
            )
            break
        except:
            messages.pop(1)

    return res.choices[0].message.content


async def main():
    await get_message([{"role": "user","content": "Explain the role of artificial intelligence in contemporary society, covering its impact on industries, daily life, and potential future developments. Include key examples and milestones."}])


if __name__ == '__main__':
    asyncio.run(main())
