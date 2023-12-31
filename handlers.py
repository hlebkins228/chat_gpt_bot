from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from random import choice

import text
from openai_requests import get_chat_gpt_response


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(text.start_message)


@router.message()
async def user_request_handler(message: Message):
    await message.answer(choice(text.waiting_list))
    answer_text = get_chat_gpt_response(message.text)
    await message.answer(answer_text)

