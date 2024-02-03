import asyncio

from openai import OpenAI

import config

client = OpenAI(api_key=config.OPENAI_API_KEY)


def api_request(messages: list):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return completion.choices[0].message


async def get_message(messages: list):
   loop = asyncio.get_event_loop()
   res = loop.run_in_executor(
       None,
       api_request,
       messages
   )
   return res


async def main():
    await get_message([{"role": "user","content": "Explain the role of artificial intelligence in contemporary society, covering its impact on industries, daily life, and potential future developments. Include key examples and milestones."}])


if __name__ == '__main__':
    asyncio.run(main())
