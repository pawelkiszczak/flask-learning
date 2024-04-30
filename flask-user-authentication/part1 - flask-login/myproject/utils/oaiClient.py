from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class MottoGenerator():
    def __init__(self):
        self.model = 'gpt-3.5-turbo'
        self.system_prompt = "Jesteś twórczym wieszczem, potrafiącym podnieść każdego na duchu swoją twórczością."
        self.client = OpenAI()

    def generate(self, username):

        user_motto = f"Napisz wesołe i zabawne motto na dzisiejszy dzień dla użytkownika o imieniu {username}."

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_motto}
        ]

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )

        generated_motto = completion.choices[0].message.content

        return generated_motto