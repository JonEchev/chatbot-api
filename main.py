from fastapi import FastAPI, UploadFile, File
from Context import reset_context, update_context
from ChatGptDynamicIA import chat_gpt_response, transcribe_audio

## Instancia de FastAPI() para la creacion del bot
app=FastAPI()

## Descripcion: Esta Clase esta invocando a la clase ChatGptDynamicIA, puede invocar a las 3 porque las 3 son independientes y cada una mas avanzada que la otra.

## EndPoint de prueba
@app.get("/")
def read_root():
    return {"Mensaje": "Mi Hola Mundo Con FastAPI()"};


## EndPoint que permite resetear el contexto desde navegador web; si el fichero json no existe, se crea, pero si existe, se actualizaria su valor
## Se debe ejecutar siempre primero este EndPoint
@app.post("/reset/")
def reset(my_context="Eres un Director de una de las areas de desarrollo de Google, respondes en español latino y siempre hablas con ironia, pero eres muy amable. Siempre termina con una pregunta para continuar con la entrevista y usa 30 palabras como mucho."):
    reset_context(my_context)
    return {"message": "reseted context"};


## Funcion centralizada para mandar el texto directamente al context del ChatBot
def send_message_to_chat(message):
    msg = {
        "role": "user",
        "content": message
    }
    update_context(msg)
    
    respuesta = chat_gpt_response()
    msg = {
        "role": "assistant",
        "content": respuesta
    }
    update_context(msg)
    return respuesta
    

## EndPoint que permite chatear con el ChatBot via web, asincrono porque la peticion es hacia el servidor
@app.post("/send-message/")
async def send_message(message):
    respuesta = send_message_to_chat(message)
    return {"response": respuesta}


## EndPoint para subir un fichero de audio tipo file
@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):
    
    ## Guardar el fichero fisicamente dentro del repositorio al subirlo
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
        
    ## Convertir el fichero de audio para lectura
    audio_input = open(file.filename, "rb")
        
    ## Convertir el fichero de audio a texto
    message = transcribe_audio(audio_input)
    
    print("audio transcrito: ", message)
    respuesta = send_message_to_chat(message)
    
    print(f"respuesta {respuesta}")
    return {"response": respuesta}