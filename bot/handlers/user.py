from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from bot.keyboards import reply, inline
from requestion.requestion import save_html_page, weather_data


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Здесь ты можешь:', reply_markup=reply.main_kb)


@router.message(F.text.lower() == "погода сейчас")
async def weather_button(message: Message):
    await message.answer(f"Погода сейчас")


@router.message(F.location)
async def location_handler(message: Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    save_html_page(latitude, longitude)
    weather_inf = weather_data()
    print(weather_inf["temp"])

    await message.answer(f"{weather_inf["temp"]} градусов, {weather_inf["condition"]}\n"
                         f"ветер {weather_inf["wind_speed"]} м/с с {weather_inf["wind_from"]}")


@router.message(F.text.lower())
async def echo(message: Message):
    await message.answer(f"Моя твоя не понимать")


@router.callback_query(F.data == "btn_geo")
async def btn_geo(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(f"asd")