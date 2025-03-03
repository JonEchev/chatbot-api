import json

CONTEXT_FILE="context.json"

## funcion para cargar el contexto, retornado el fichero json
def load_context():
    try:
        with open(CONTEXT_FILE,"r",encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []    

## funcion para guardar el contexto de un fichero json
def save_context(context):
    with open(CONTEXT_FILE,"w",encoding="utf-8") as file:
        json.dump(context,file,ensure_ascii=False,indent=4)
        
## funcion para actualizar el contexto con un mensaje
def update_context(message):
    context=load_context()
    ## agregar un nuevo dato al fichero json
    context.append(message)
    save_context(context)

## funcion para resetear el context
def reset_context(initial_context="Eres el jefe del departamento de tecnologia. "):
    context=[
        {"role":"system","context":initial_context}
    ]
    
    save_context(context)
    
    
## probar el llamado a la funcion reset_context()
if __name__ == "__main__":
    reset_context()