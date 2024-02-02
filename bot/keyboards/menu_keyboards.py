from aiogram.utils.keyboard import InlineKeyboardBuilder

menu_keyboard = InlineKeyboardBuilder()
# Cписок кнопок из гугл таблицы
for button in ["МТС", "Билайн", "ВК", "Тинькофф"] + ["😇 Свободный диалог"]:
    menu_keyboard.button(text=button)
menu_keyboard = menu_keyboard.as_markup()
