# Aplicación de introducción a Flask

Programa hecho en python con el framework flask, Hello word

# Instalación
- crear un entorno en python y ejecutar el comando
```
pip install -r requirements.txt
```
la libreria utilizada en flask https://flask-wtf.readthedocs.io/en/1.2.x/

# Ejecucion del programa
 -iniciar el servidor de flask
 -en mac: 
  ```export FLASK_APP=main.py```
 -en windows:
  ```set FLASK_APP=main.py```

# Otra opción de ejecución 
  -crear un archivo .env y dentro agregar los siguiente:
  ``` FLASK_APP=main.py ```
  ``` FLASK_DEBUG=True ```
  -y luego poder ejecutar en la terminal el comando:
  ``` flask run ```

# Comando para ejecutar el servidor
 ```flask --app main run```

# Comando para ejectuar el servidor en otro puerto diferente por default siempre es el 5000
```flask --app main run -p 5002```

# Comando para ejecutar el servidor en modo debug, para realizar cambios en tiempo real
```flask --app main --debug run```