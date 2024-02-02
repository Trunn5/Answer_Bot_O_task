from aiogram.utils.keyboard import InlineKeyboardBuilder

k = InlineKeyboardBuilder()
# Cписок кнопок из гугл таблицы
for button in ["МТС", "Билайн", "ВК", "Тинькофф"] + ["😇 Свободный диалог"]:
    k.button(text=button)
k = k.as_markup()
