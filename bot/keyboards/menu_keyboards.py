from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def menu_keyboard() -> InlineKeyboardMarkup:
    """Составляет и возвращает клавиатуру для меню с брендами."""
    keyboard = InlineKeyboardBuilder()
    # Cписок кнопок из гугл таблицы
    for button in ["МТС", "Билайн", "ВК", "Тинькофф"] + ["😇 Свободный диалог"]:
        keyboard.button(text=button)
    keyboard = keyboard.as_markup()
    return keyboard
