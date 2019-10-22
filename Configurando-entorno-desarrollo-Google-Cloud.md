# Configurando el entorno de desarrollo de Google Cloud

Ya construimos una agenda que funciona en nuestro computador, pero que sucede si quisieramos hacer disponible nuestro programa para todo el mundo.

En este proyecto vamos a construir una agenda web que permite a todos entrar a agregar sus contacto.

Para poder subir nuestro programa vamos a usar Google App Engine.

Lo primero que debemos hacer es instalar el software de google cloud sdk.

App Engine no corre el comando pip por esto debemos subir las librerías del proyecto, para esto podemos crear una carpeta lib y en un archivo appengine-config.py podemos definir usar esta carpeta.

Ahora para instalar las dependencias usamos el comando 
```python
pip install -r requirements.txt -t lib
```

Luego podemos correr nuestro servidor con 
```python
dev_appserver.py
```
estando en el directorio del proyecto.

Para poder publicar el proyecto debemos entrar a console.cloud.google.com y crear un nuevo proyecto.

En la sección google app engine, seleccionamos el lenguaje y región.

Para realizar el deploy de la aplicación, primero debemos autenticarnos usando el comando gcloud auth login.

Ahora realizamos
```python
 gcloud app deploy --project [ID del proyecto]
 ```

Y listo tenemos el proyecto en los servidores de Google.