from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards import reply


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Hello, user', reply_markup=reply.main_kb)


@router.message(F.text.lower() == "погода сейчас")
async def weather_button(message: Message):
    await message.answer(f"Погода сейчас")


@router.message(F.text.lower())
async def echo(message: Message):
    await message.answer(f"Моя твоя не понимать")