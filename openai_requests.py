from openai import OpenAI

from config import OPENAI_TOKEN
from config import chat_gpt_model


def get_chat_gpt_response(prompt):
    client = OpenAI(api_key=OPENAI_TOKEN)
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}]

    completion = client.chat.completions.create(model=chat_gpt_model, messages=messages)

    return completion.choices[0].message.content
