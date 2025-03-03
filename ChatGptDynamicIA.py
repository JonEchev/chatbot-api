from openai import OpenAI
from decouple import config
from Context import reset_context, load_context, update_context

## obtener una variable de entorno de una clase tipo config en Python
api_key = config('OPENAI_API_SECRET_KEY')
client = OpenAI(api_key=api_key)


## funcion en python (funciona con pago en OpenAI, de lo contrario, saca: Error code: 429)
def chat_gpt_response():
    ## cargar el contexto antes de que empiece la conversacion para evitar errores
    context = load_context()
    ## definicion de completion para la version de OpenAI a usar
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=context
    )
    return completion.choices[0].message.content


## funcion para leer un fichero de audio
def transcribe_audio(audio_file):
    transcription = client.audio.transcriptions.create(
        model = "whisper-1",
        file = audio_file
    )
    return transcription.text


## condicional con Python, llamando a la funcion chat_gpt_response()
if __name__ == "__main__":
    print(f".::: Bienvenid@ :::.")
    contexto=input("Introduce el contexto (Recuerda que esta App debe pagar la cuota de manejo de OpenAI): ")
    ## aunque saca Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}
    ## si actualiza la informacion en el fichero json, para solucionar ese error 429 debo de pagar en OpenAI para uso de la extension de la IA de ChatGPT
    reset_context(initial_context=contexto)
    
    print(f"*Importante* \nAntes de empezar, ten en cuenta que si quieres finalizar la conversacion debes escribir la palabra: exit")
    entrada=input("Introduce un mensaje: ")
    ## bucle con python
    while entrada != "exit":
        message={
            "role": "user",
            "content": entrada
        }
        update_context(message)
        respuesta = chat_gpt_response()
        
        message={
            "role": "assistant",
            "content": respuesta
        }
        update_context(message)
        print(f"respuesta {respuesta}")
        entrada=input("Introduce un mensaje: ")
        
    print(f"...ChatBot finalizado...")