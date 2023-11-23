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
Antes de ejecutar la aplicación, asegúrate de configurar la conexión a tu base de datos en el archivo config.py. Proporciona la URL de conexión y cualquier otra configuración necesaria.

```bash
# config.py

DATABASE_URI = "tu_url_de_base_de_datos"
```

## Ejecutar la Aplicación
Una vez que has configurado el entorno virtual, instalado las dependencias y configurado la base de datos, puedes ejecutar la aplicación con el siguiente comando:

```bash
python main.py [AMBIENTE]
```

Debe indicar el ambiente para el cual desa correr el backend, esto se logra remplazando [AMBIENTE] por `dev` para desarrollo y `prod` para produccion, en caso de no enviar el ambiente por defecto se ejecutara para desarrollo.

La aplicación se ejecutará en `http://127.0.0.1:5000/` por defecto.

## Endpoints
La API proporciona los siguientes endpoints:

* `/api/productos`: Obtiene la lista de productos.
* `/api/productos/{id}`: Obtiene detalles de un producto específico.
* `/api/carrito`: Gestiona el carrito de compras.

Otros endpoints según las necesidades específicas del proyecto.

## Contribuciones
¡Contribuciones son bienvenidas! Si tienes sugerencias, mejoras o encuentras problemas, por favor, abre un issue o envía un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para obtener más detalles.