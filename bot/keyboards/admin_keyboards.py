from aiogram.utils.keyboard import InlineKeyboardBuilder

update_data_keyboard = InlineKeyboardBuilder() \
    .button("Обновить данные🔄", callback_data="update_data")
