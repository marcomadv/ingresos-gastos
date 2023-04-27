# Aplicación web Ingresos-gastos

Programa hecho en python con el framework flask, Hello world.

# Instalación

- crear un entorno en python y ejecutar el comando
```
pip install -r requirements.txt
```
la libreria utilizada en flask https://flask.palletsprojects.com/en/2.2.x/

# Ejecuciond el progama
- inicializar el servidor de flask:

en mac:``` export FLASK_APP=main.py```
en windows: ```set FLASK_APP=main.py```

# Otra opcion para ejecutar
- crear un archivo .env y agregar lo siguiente:
```FLASK_APP=main.py````
```FLASK_DEBUG=True````
- posteriormente lanza en el terminal el comando:
```flask run```

# Comando para ejecutar el servidor:
```flask --app main run```

# Comando para ejecutar servidor en otro puerto diferente, por default es el 5000
```flask -app main run -p 5002```

# Comando para ejecutar el servidor en modo debug, para realizar cambios en tiempo real 
```flask --app main --debug run```

