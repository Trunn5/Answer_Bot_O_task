import asyncio

from loader import dp, bot
from set_commands_to_menu import set_commands_to_menu

from handlers import *


async def on_startup(bot):
    await set_commands_to_menu(bot)


if __name__ == '__main__':
    asyncio.run( dp.start_polling(bot, on_startup=on_startup(bot)) )

