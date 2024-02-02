from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.utils.sheet_filter import get_next_parameters


def parameter_keyboard(current: list[str]) -> InlineKeyboardMarkup:
    """
    Составляет и возвращает клавиатуру для следующего параметра в зависимости от текущего
    :param current: Текущий ряд параметров, например: ["Мтс", "От агента"]
    :return: Клавиатура с возможными вариантами параметров
    """

    next_parameters = get_next_parameters(current)

    keyboard = InlineKeyboardBuilder()

    # callback: question_{id параметра}_{номер по списку}
    for i, button in enumerate(next_parameters):
        keyboard.button(text=button, callback_data=f"question_{len(current)}_{i}")

    # Начальное меню -> добавить свободный диалог
    if len(current) == 0:
        keyboard.button(text="😇 Свободный диалог", callback_data=f"/ai")


    keyboard.adjust(1)
    keyboard = keyboard.as_markup()
    return keyboard
