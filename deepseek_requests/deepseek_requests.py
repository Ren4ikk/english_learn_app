import requests
import json
from dotenv import load_dotenv
import os


class DeepSeekRequest:
    def __init__(self):
        load_dotenv()
        self.API_KEY = os.getenv("API_KEY")
        self.MODEL = "deepseek/deepseek-r1:free"

    def process_content(self, content):
        return content.replace('<think>', '').replace('</think>', '')

    def chat_stream(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": self.MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": True
        }

        with requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data,
                stream=True
        ) as response:
            if response.status_code != 200:
                print("Ошибка API:", response.status_code)
                return ""

            full_response = []

            for chunk in response.iter_lines():
                if chunk:
                    chunk_str = chunk.decode('utf-8').replace('data: ', '')
                    try:
                        chunk_json = json.loads(chunk_str)
                        if "choices" in chunk_json:
                            content = chunk_json["choices"][0]["delta"].get("content", "")
                            if content:
                                cleaned = self.process_content(content)
                                # print(cleaned, end='', flush=True)
                                full_response.append(cleaned)
                    except:
                        pass

            print()  # Перенос строки после завершения потока
            return ''.join(full_response).replace('*', '').replace('---', '').replace('###', '')

    def deep_seek_request(self, user_input):
        return self.chat_stream(user_input)
