from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import text


reply_keyboard_buttons = [
    [KeyboardButton(text=text.button_new_session_text)],
    [KeyboardButton(text=text.button_new_model_text)],
    [KeyboardButton(text=text.button_manual_text)],
    [KeyboardButton(text=text.button_callback_text)]
                          ]
reply_keyboard = ReplyKeyboardMarkup(keyboard=reply_keyboard_buttons, resize_keyboard=True, one_time_keyboard=True)
