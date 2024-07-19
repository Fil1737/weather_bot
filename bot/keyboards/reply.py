from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Погода сейчас")
        ]
    ],
    resize_keyboard=True
)

