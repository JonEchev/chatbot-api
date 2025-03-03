# random-food-app

API de un ChatBot en Python.

> <p>#python #openai #fastapi</p>

---

## Tabla de Contenido

- [Descripción](#descripción)
- [Construido con](#construido-con)
- [Desarrollo](#desarrollo)
- [Endpoints](#endpoints)
- [Autor y contacto](#autor-y-contacto)

---

## Descripción

API de un ChatBot utilizando a ChatGPT de OpenAI (versión pagada de cuota de manejo).

---

## Construido con

El código se encuentra implementado con Python y OpenAI usando la siguiente librería:

- OpenAI - Para la importación y utilización de ChatGPT
- FastAPI - Framework web de Python que permite crear aplicaciones web de manera rápida y eficiente

---

## Desarrollo
1. Instale en el equipo un IDE de desarrollo como Visual Studio Code (VS Code) y posteriormente los siguientes plugins o extensiones: Python o Python3, Python for VSCode, Python Indent, Python Environment Manager (deprecated), autoDocstring - Python Docstring Generator y Python Extension Pack.
2. Instale node, npm y yarn en el mismo equipo (PC).
3. Clone este repositorio desde GitHub: https://github.com/JonEchev/chatbot-api rama: main.
4. Logueese en: https://platform.openai.com/api-keys y cree una Secret Key.
5. Inicialice el proyecto, desde Visual Studio Code
6. Valide que las librerias esten correctamente instaladas en el IDE y que la SECRET KEY que creo en OpenAI este correctamente diligenciada en la variable de entorno: OPENAI_API_SECRET_KEY del archivo .env
7. Elimine la carpeta .venv (si esta existe) y abra un terminal dentro de VS Code y cree un entorno virtual de Python, ejecutando el comando: python3 -m venv .venv
8. En el mismo terminal y sino se ha activado (sino tiene (.venv) al inicio de la linea de comando en el Terminal), activa el entorno virtual con el siguiente comando: source .venv/bin/activate
9. En el mismo terminal, ejecute el comando: python3 -m pip install openai
10. Luego, en el mismo terminal, ejecute el comando: python3 -m pip install openai python-decouple
11. En el mismo terminal, ejecute el comando: python3 -m pip install fastapi uvicorn
12. En el mismo terminal, ejecute el comando: python3 -m pip install python-multipart
13. Abra un terminal dentro de VS Code e ingrese el siguiente comando: python3 -m uvicorn main:app --reload ó uvicorn main:app --reload
14. Posteriormente al ejecutar el punto (13), la documentación Swagger del backend se encuentra en la siguiente ruta: http://127.0.0.1:8000/docs
15. Ya puede validar los endpoint con el "Try it out" de Swagger
16. Para finalizar la ejecución de uvicorn, en el Terminal de VS Code, pulsar al mismo tiempo las dos teclas: ctrl + c
17. Para finalizar la ejecución del entorno virtual, ejecute en el Terminal de VS Code el comando: deactivate


## Endpoints Web

- **LOCAL**
    - API (GET): http://127.0.0.1:8000/docs#/default/read_root__get
    - API (POST): http://127.0.0.1:8000/docs#/default/reset_reset__post
    - API (POST): http://127.0.0.1:8000/docs#/default/send_message_send_message__post
    - API (POST): http://127.0.0.1:8000/docs#/default/post_audio_post_audio__post

## Autor y contacto

- **Nombre**: Jonatan Echeverry
- **Correo electrónico**: jonechev1@gmail.com
- **GitHub**: [@JonEchev](https://github.com/JonEchev)
- **LinkedIn**: [jonatan-echeverry](https://www.linkedin.com/in/jonatan-echeverry-7130251a0/)
- **Blog:** [Crazy Genius!](https://crazycuestionct.blogspot.com/search/label/Programaci%C3%B3n)