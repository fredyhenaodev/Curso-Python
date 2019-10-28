# Configuración del ambiente
Anaconda es una instalación de Python que ya trae preinstalado todos los paquetes necesarios para tu labor en la Ciencia de Datos, tiene más de 1400 paquetes. Nos permite configurar ambientes virtuales para poder utilizar diferentes versiones de nuestros paquetes.


* ```python conda --version ```  para conocer la versión y saber que lo tenemos instalado
* ```python conda --help ``` nos da todos los comandos que podemos usar.
* ```python conda list ``` nos lista todos los paquetes que Anaconda instaló.

Una buena práctica es generar un ambiente virtual por cada proyecto, los ambientes virtuales nos permiten generar varios proyectos con diferentes versiones de la librería sin generarnos errores de compatibilidad. Tradicionalmente en Python se utiliza virtualenv

```python
conda create --name [nombre-del-proyecto] [librerías-a-usar]
conda create --name platzi_data beautifulsoup4 requests numpy pandas matplotlib yaml
source activate platzi_data //Para activar
source deactivate //Para salir

conda env list //nos muestra los ambientes virtuales que tenemos
conda remove --name [nombre-del-proyecto] --all //eliminar nuestro entorno virtual con todos nuestros paquetes
```