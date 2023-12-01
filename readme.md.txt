# Pasos para iniciar el backend

1. Usar el comando: venv/Scripts/activate

2. Usar el comando: pip install -r requirements.txt

3. usar el comando: uvicorn main:app --reload

# Pasos para iniciar el frontend

1. usar el comando npm i

2. usar el comando npm run dev

## PASOS EXTRAS

* Si el servidor inicia en una ruta diferente al localhost:3000, en el main.py cambiar el numero de el localhost en la variable origins al numero del localhost donde inicio el frontend.

* Si da error al ejecutar el comando venv/Scripts/activate, borrar la carpeta venv y ejecutar el siguiente comando: python3 -m venv venv y volver a ejecutar los comandos.

* Si da error por scripts de powershell, buscar como ejecutar scripts en powershell y activar esta opcion; luego ejecutar los comando de nuevo.

* Si da errores por pip, instalar pip desde la tienda de windows, o buscar como activar la variable de entorno de python; luego volver a ejecutar los comandos.