from aiogram import Bot
from aiogram.methods import SetMyCommands
from aiogram.types import BotCommand


async def set_commands_to_menu(bot: Bot) -> None:
    """
    Устанавливает команды в боковое синее меню бота.
    :param bot: Бот для установки.
    :return: None
    """
    await bot(SetMyCommands(commands=[
        BotCommand(command='menu', description='⬇️Главное меню'),
        BotCommand(command='ai', description='🔥Свободное общение'),
    ]))