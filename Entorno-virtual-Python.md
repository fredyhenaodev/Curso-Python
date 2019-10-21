## Entorno virtual en Python
En Python la comunidad comparte su código usando PyPi (python package index), es un repositorio para instalar módulos de la comunidad.

Con pip install [nombre] se puede instalar el paquete que deseas.

Podemos utilizar requirements.txt para ordenar los paquetes que requiere tu proyecto.

### Ambiente virtual

Nos permite encapsular un proyecto para poder instalar las versiones de los paquetes que se requieran sin tenerlos que instalar en todo el sistema operativo.

### Crear un entorno virtual

Dentro de la carpeta de tu proyecto ejecutas

```linux
virtualenv venv
```

### Encender un entorno virtual

```linux
source venv/bin/activate
```

### Ver las dependencias instaladas en el entorno virtual

```linux
pip freeze
```

### Instalar dependencias del archivo requirements

```linux
pip install -r requirements.txt
```
