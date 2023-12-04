# PetWay API - Backend para PetWay Frontend

PetWay API es el backend que proporciona los endpoints necesarios para el funcionamiento del frontend PetWay. Este proyecto está diseñado para gestionar la lógica del servidor y la interacción con la base de datos para satisfacer las necesidades del frontend.

## Instalación y Configuración

### Crear un Entorno Virtual (Virtual Environment)

Se recomienda utilizar un entorno virtual para aislar las dependencias del proyecto. Puedes crear un entorno virtual con el siguiente comando:

```bash
python -m venv venv
```

### Activar el Entorno Virtual
En sistemas basados en Unix/Linux:

```bash
source venv/bin/activate
```

En sistemas basados en Windows:

```bash
venv\Scripts\activate
```

### Instalar Dependencias
Las dependencias del proyecto están especificadas en el archivo `requirements.txt`. Para instalarlas, utiliza el siguiente comando:

```bash
pip install -r requirements.txt
```
Este comando instalará todas las dependencias necesarias para ejecutar el proyecto.

### Agregado de dependencias
Si en algun momento necesita agfegar dependencias al archivo `requirements.txt` puede ejecutar el siguiente comando:
```bash
pip freeze > requirements.txt
```
El mismo va a tomar las dependencias que encuentre y las va actualizar en el archivo de requerimientos en caso de que ya existan o generar uno nuevo caso contrario.


## Configuración de la Base de Datos
Antes de ejecutar la aplicación, asegúrate de configurar la conexión a tu base de datos en el archivo configXXXX.py. Proporciona la informacion solicitada de conexión y cualquier otra configuración necesaria.

```bash
# configXXXX.py

    Config.ENV = 'Ambiente donde se va a trabajar'
    Config.DEBUG = 'Valor boolean (True/False) para activar el modo debug'
    Config.TESTING = 'Valor boolean (True/False) para activar el modo debug'
    Config.SECRET_KEY = 'Valor secreto para desbloquear la consola'
    Config.PORT_APP = 'Valor numérico del puerto donde se va a ejecutar la api'
    Config.SERVER_NAME = 'Nombre del servidor'
    USER_DB = 'Usuario para acceder a la base de datos'
    PASS_DB = 'Clave para acceder a la base de datos'
    HOST_DB = 'Servidor donde se encuentra la base de datos'
    PORT_DB = 'Puerto en el que corre la base de datos'
    NAME_DB = 'Nombre de la base de datos'

# No es necesario alterar la siguiente linea, ya que toma los datos de los provistos anteriormente.
    SQLALCHEMY_DATABASE_URI= 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USER_DB,PASS_DB,HOST_DB,PORT_DB,NAME_DB)
```
Antes de pasar a ejecutar la aplicación hay que asegurarse que la DB se encuentra creada en el servidor, una vez verificado esto y configurado el archivo de configuracion pertinente se puede mandar a correr la aplicacion, no se
preocupe por las tablas ya que el ORM se encarga de crear las que haga falta o modificar las existentes.

## Ejecutar la Aplicación
Una vez que has configurado el entorno virtual, instalado las dependencias y configurado la base de datos, puedes ejecutar la aplicación con el siguiente comando:

```bash
python main.py [AMBIENTE]
```

Debe indicar el ambiente para el cual desa correr el backend, esto se logra remplazando [AMBIENTE] por `dev` para desarrollo y `prod` para produccion, en caso de no enviar el ambiente por defecto se ejecutara para desarrollo.

La aplicación se ejecutará en `http://127.0.0.1:5000/` por defecto.

## Endpoints
La API proporciona los siguientes endpoints:

* `/question/create`: [POST] permite almacenar en la base de datos las consultas realizadas.


Otros endpoints según las necesidades específicas del proyecto.

## Contribuciones
¡Contribuciones son bienvenidas! Si tienes sugerencias, mejoras o encuentras problemas, por favor, abre un issue o envía un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para obtener más detalles.