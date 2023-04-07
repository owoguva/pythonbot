from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot



async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_2")
    markup.add(button_1)

    question = "Кто написал Евгений Онегин?"
    answer = [
        "Лермонтов",
        "Гоголь",
        "Пушкин",
        "Толстой",
        "Путин",
        "Достоевский"
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )


    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Стыдно не знать",
        open_period=10,
    )

# @dp.message_handler()
async def echo(message: types.Message):
    try:
        num = float(message.text)
        await message.answer(str(num**2))
    except ValueError:
        await message.answer(message.text)

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
    dp.register_callback_query_handler(echo)