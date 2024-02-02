import asyncio

from loader import bot
from bot.utils.set_commands_to_menu import set_commands_to_menu

from handlers import *


async def main():
    print("Запуск бота")
    await set_commands_to_menu(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

