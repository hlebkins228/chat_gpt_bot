from openai import OpenAI

from config import OPENAI_TOKEN
from config import chat_gpt_model


def get_chat_gpt_response(prompt, messages):
    client = OpenAI(api_key=OPENAI_TOKEN)
    messages.append({"role": "user", "content": prompt})

    completion = client.chat.completions.create(model=chat_gpt_model, messages=messages)
    chat_response_text = completion.choices[0].message.content

    messages.append({"role": "assistant", "content": chat_response_text})

    return chat_response_text, messages
