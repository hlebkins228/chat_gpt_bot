from aiogram.fsm.state import StatesGroup, State


class BotStates(StatesGroup):
    change_model_state = State()
    chat_gpt_request_state = State()
    callback_state = State()
