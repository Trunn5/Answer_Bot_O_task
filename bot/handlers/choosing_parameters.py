from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, CallbackQuery

from bot.handlers import ai_callback, ai_message
from bot.keyboards import parameter_keyboard
from bot.loader import dp, get_sheet_data
from bot.utils.sheet_filter import get_next_parameters


@dp.callback_query(F.data.startswith("question_"))
async def choosing_parameters(q: types.CallbackQuery, state: FSMContext):
    """
    Обрабатывает Inline кнопку с выбором параметра.

    :param q: callback type question_{стадия опроса}_{номер в списке}
    """
    stage, prev = map(int, q.data.split('_')[1:])

    # Если пропускаем
    if prev == -1:
        chosen = 'Пропустить'
    else:
        # Собираем предыдущие параметры
        prev_parameters = []
        for line in  q.message.reply_markup.inline_keyboard:
            prev_parameters += [button.text for button in line]
        chosen = prev_parameters[prev]
        await q.answer(f"Выбрано: {chosen}")

    # Добавляем выбор пользователя в data
    data = (await state.get_data()).get('form', [])
    data += [chosen]
    await state.set_data({'form': data})


    sheet_data = get_sheet_data()

    # Заканчиваем опрос если опросили всё до промта, начинаем диалог
    if stage == len(sheet_data[0]) - 2:
        prompt = get_next_parameters(data)[0]
        await ai_message(q.message, state, prompt=prompt)
        return

    markup: InlineKeyboardMarkup = parameter_keyboard(data)
    if markup.inline_keyboard[0][0].text == "Пропустить":
        q = CallbackQuery(id=q.id, from_user=q.from_user, chat_instance=q.chat_instance, message=q.message, data=f"question_{stage+1}_-1")
        await choosing_parameters(q, state)
        return

    await q.message.edit_text(sheet_data[0][len(data)], reply_markup=markup)


