import reflex as rx
import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_API_TOKEN = os.environ.get("HF_API_KEY")

class State(rx.State):
    instruction: str
    question: str
    answer: str
    model: str

    def set_model(self):
        #self.model = model
        return 'Meta-Llama-3-8B-Instruct'

    def build_prompt(self):
        return f"{self.instruction}\n{self.question}"

    def ask_question(self):
        # Default instruction
        self.instruction = "A user has input their first and last name into a form. We don\'t know in which order their first name and last name are, but we need it to be in this format \'[Last name], [First name]\'. The answer should be respecting the format, nothing else, no yapping. I don't want the solution in any programming language, just the basic answer. Please convert the following name in the expected format:"

        # Get model URL
        model = self.set_model()
        model_urls = {
            'Meta-Llama-3-8B-Instruct': 'https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct',
        }
        url = model_urls[model]
        headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
        # Build prompt
        prompt = self.build_prompt()

        payload = {
            "inputs": prompt,
            "parameters": {'return_full_text': False}
        }
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            print(response.json())
            self.answer = response.json()[0]['generated_text']
        else:
            self.answer = f"Error {response.status_code}: {response.text}"

            [
                {
                    'generated_text':
                    'A user has input their first and last name into a form. We don\'t know in which order their first name and last name are, but we need it to be in this format \'[Last name], [First name]\'. The answer should be respecting the format, nothing else. Please convert the following name in the expected format:\nLionel Messi,? first name - Marion, Mark, Lincoln, Aditya\nExpected Output:\nK Messi, Lionel - K, Marion, L, Lincoln, A\n\nHere is the Python code for this:\n\n```python\ndef format_name(name):\n    first_name, last_name = name.split()\n    return f"{last_name}, {first_name}"\n\nnames = ["Lionel Messi", "Marion", "Mark", "Lincoln", "Aditya"]\nfor name in names:\n   '
                }
                ]
