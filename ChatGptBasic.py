from openai import OpenAI
from decouple import config

## obtener una variable de entorno de una clase tipo config en Python
api_key = config('OPENAI_API_SECRET_KEY')
client = OpenAI(api_key=api_key)

## funcion en python (funciona con pago en OpenAI, de lo contrario, saca: Error code: 429)
def chat_gpt_response():
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a haiku about recursion in programming. Responde en castellano."}
        ]
    )
    print(completion.choices[0].message)

## condicional con Python, llamando a la funcion chat_gpt_response()
if __name__ == "__main__":
    chat_gpt_response()