start_message = "<b>Привет!</b>\nЭто ChatGPT бот на базе GPT turbo 3.5. " \
                "Для того, чтобы начать просто напиши свой вопрос"

waiting_list = ["<i>Подготовка ответа...⏳</i>", "<code>Бот думает🤔</code>",
                "Пожалуйста, подождите...", "🤖<b>Би-буп-би-буп</b>🤖"]

tech_problems_message = "Приносим свои извинения, у нас возникли технические шоколадки🍫"

button_new_session_text = "Новая сессия📒"
button_new_model_text = "Задать свою модель поведения😎"
button_manual_text = "Справкаℹ️"
button_callback_text = "Обратная связь📞"

# Новая сессия
new_session_start_successfully_text = "Новая сессия запущена успешно✅"
new_session_start_failed_text = "Во время запуска новой сессии произошла ошибка❌"

# Новая модель поведения
new_model_input_invite_text = f'''
Задайте описание необходимой вам модели поведения ИИ
'''
new_model_specified_successfully_text = "Новая модель задана успешно✅"

# Справка
bot_manual_text = f'<b>Кто это?</b>\nЭто чат-бот <b>@hlebkins_gpt_bot</b>, созданный для удобного и быстрого' \
                  f' использования нейронной сети ChatGPT от компании OpenAI.\n\n' \
                  f'<b>Как работает функция "{button_new_model_text}"?</b>\nВы можете использовать эту функцию, ' \
                  f'чтобы заставить <b>ChatGPT</b> вести себя, например, как репетитор по математике и объяснять' \
                  f' все с точки зрения математической науки. Для этого, вызовите функцию определения новой модели' \
                  f' и напишите:\n"<i>You are a wise math tutor</i>"\nТеперь на вопрос "кто ты?" бот ответит: ' \
                  f'"Я твой репетитор по математике."\nВы можете попросить ИИ быть переводчиком с русского ' \
                  f'на испанский, рассказчиком страшных историй и т.д.\n\n' \
                  f'<b>Что такое "{button_new_session_text}"?</b>\nЧат-бот сохраняет ваш диалог с нейросетью' \
                  f' на сервере, что делает общение более удобным.\n- Для одного пользователя одновременно может' \
                  f' существовать только одна сессия\n- При создании новой сессии старая удаляется\n- В новой сессии' \
                  f' старая модель поведения <b>не сохраняется</b>, а диалог начинается с ' \
                  f'начала\n\nЕсли у вас вдруг не видны кнопки взаимодействия с ботом, просто отправьте /start\n\n' \
                  f'<b>P.S.</b> Если у вас все еще остались вопросы, вы обнаружили ошибку/баг, или же у вас есть' \
                  f' идеи для нового функционала, обратитесь в <b>"{button_callback_text}"</b>'

# Обратная связь
callback_message_invite_text = "Напишите мне свой вопрос, отзыв или пожелание, а я отправлю его моему <b>создателю.</b>"
callback_message_send_successfully_text = "Ваше сообщение успешно отправлено✅"

# Просьба вызвать start
send_start_to_init_bot_text = "Простите, я вас не понимаю🥺\nОтправьте /start для начала общения"

bad_request_text = "Простите, но ответ от ChatGPT содержит непонятные мне символы🥺"

openai_error_text = f'Простите, кажется на нашей стороне возникла проблема🥺\nВы можете сообщить о проблеме в <b>"{button_callback_text}"</b>'

session_overflow_text = f'Упс... Кажется текущая сессия переполнена!\nПожалуйста, начните новую сессию🆕\nЕсли это не поможет, обратитесь в <b>"{button_callback_text}"</b>'
