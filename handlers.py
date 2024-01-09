from aiogram.exceptions import TelegramBadRequest
from aiogram import Router, F, Bot
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import BotStates

from random import choice

import text
from openai_requests import get_chat_gpt_response
from db import *
from keyboard import reply_keyboard
from config import BOT_TOKEN, admin_id

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
router = Router()

db_connect_status, db_connect_thread = db_connect()


@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    await state.set_state(BotStates.chat_gpt_request_state)
    await message.answer(text.start_message, reply_markup=reply_keyboard)


@router.message(F.text == text.button_new_session_text)
async def new_session_button_hendler(message: Message):
    if db_connect_status:
        response = db_get_user_filename(db_connect_thread, message.from_user.id)
        if response[0]:
            filename = response[1]
        else:
            filename = db_add_user(db_connect_thread, message.from_user.id, message.from_user.username)

        clear_user_messages(filename)
        await message.answer(text.new_session_start_successfully_text)
    else:
        await message.answer(text.new_session_start_failed_text)


@router.message(F.text == text.button_new_model_text)
async def change_model_button_hendler(message: Message, state: FSMContext):
    await message.answer(text.new_model_input_invite_text)
    await state.set_state(BotStates.change_model_state)


@router.message(F.text == text.button_manual_text)
async def manual_button_hendler(message: Message):
    await message.answer(text.bot_manual_text)


@router.message(F.text == text.button_callback_text)
async def callback_button_hendler(message: Message, state: FSMContext):
    await message.answer(text.callback_message_invite_text)
    await state.set_state(BotStates.callback_state)


@router.message(BotStates.callback_state)
async def callback_message_send_hendler(message: Message, state: FSMContext):
    new_text = f"Отправитель: {message.from_user.username}\n\n<b>Сообщение:</b>\n{message.text}"

    await bot.send_message(chat_id=admin_id, text=new_text)
    await state.set_state(BotStates.chat_gpt_request_state)
    await message.answer(text.callback_message_send_successfully_text)


@router.message(BotStates.change_model_state)
async def new_model_hendler(message: Message, state: FSMContext):
    if db_connect_status:
        response = db_get_user_filename(db_connect_thread, message.from_user.id)
        if response[0]:
            filename = response[1]
        else:
            filename = db_add_user(db_connect_thread, message.from_user.id, message.from_user.username)

        change_user_model(filename, message.text)
        await state.set_state(BotStates.chat_gpt_request_state)
        await message.answer(text.new_model_specified_successfully_text)
    else:
        await message.answer(text.new_session_start_failed_text)


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

        try:
            await message.answer(response[0], reply_markup=reply_keyboard, disable_web_page_preview=True)
        except TelegramBadRequest:
            await message.answer(text.bad_request_text)
        else:
            save_user_messages(filename, response[1])
    else:
        await message.answer(text.tech_problems_message)
