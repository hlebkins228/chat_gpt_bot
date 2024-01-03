from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from random import choice

import text
from openai_requests import get_chat_gpt_response
from db import *


router = Router()

db_connect_status, db_connect_thread = db_connect()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(text.start_message)


@router.message()
async def user_request_handler(message: Message):
    await message.answer(choice(text.waiting_list))     # Отправляет сообщение о том, что запрос принят в обработку

    if db_connect_status:
        response = db_get_user_filename(db_connect_thread, message.from_user.id)
        if response[0]:
            filename = response[1]
        else:
            filename = db_add_user(db_connect_thread, message.from_user.id, message.from_user.username)

        user_messages_list = get_user_messages(filename)
        response = get_chat_gpt_response(message.text, user_messages_list)

        await message.answer(response[0])

        save_user_messages(filename, response[1])
    else:
        await message.answer(text.tech_problems_message)
