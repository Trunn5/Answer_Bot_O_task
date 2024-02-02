from aiogram.utils.keyboard import InlineKeyboardBuilder

update_data_keyboard = InlineKeyboardBuilder() \
    .button(text="Обновить данные🔄", callback_data="update_data") \
    .as_markup()
