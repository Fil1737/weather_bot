from aiogram. types import InlineKeyboardMarkup, InlineKeyboardButton

main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Узнать погоду", request_location=True, callback_data="btn_geo")
        ]
    ]
)