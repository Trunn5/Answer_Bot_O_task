from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config


sheet_data = []


def change_sheet_data(data: list):
    global sheet_data
    sheet_data = data


def get_sheet_data():
    return sheet_data


bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


