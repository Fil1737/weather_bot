from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Посмотреть погоду", request_location=True, callback_data="btn_geo")
        ]
    ],
    resize_keyboard=True
)

