from openai import OpenAI
from decouple import config

## obtener una variable de entorno de una clase tipo config en Python
api_key = config('OPENAI_API_SECRET_KEY')
client = OpenAI(api_key=api_key)

audio_file = open("audios/00_audio_initial.mp3", "rb")
transcription = client.audio.transcriptions.create(
    model = "whisper-1",
    file = audio_file
)

print(transcription.text)