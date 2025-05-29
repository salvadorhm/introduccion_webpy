# Hola mundo del web.py

## 1. Ejemplo base

El siguiente código es una simplificación del ejemplo base de [web.py](https://webpy.org/)

````python
import web

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())

class Index:
    def GET(self):
        return 'Hola mundo HTML y Python!'

if __name__ == "__main__":
    app.run()
````

## 2. Librerias

Cuando se importo la librería **web.py** utilizando **pip install web.py** se instalo el **framework**, y ahora ya se puede utilizar para desarrollar aplicaciones web.

````python
import web
````

## 3. Rutas

El **framework web.py** utiliza el **path** o **ruta** para acceder a cada una de las páginas de la aplicación, está forma permite controlar el acceso a cada página, impidiendo acceder a páginas no listadas en la **urls**.

La sintaxis para cada **ruta** es **punto de entrada** y la **clase** que controla las solicitudes y respouestas.

````python
urls = (
    '/bienvenida', 'Index'
)
````

## 4. Objeto de tipo web.py

Para la implementación de **web.py** se crea un objeto de tipo **web.application** que permite encapsular la aplicación y su funcionamiento.

````python
app = web.application(urls, globals())
````

## 5. Clase para generar un response

Cada una de las páginas web será controlada por una clase, permitiendo aplicar los conceptos de programación orientada a objetos.

- Para el renderizado de las páginas se usa de forma **obligatoria** el método **GET**.
- Para recibir datos desde un formulario se usa de forma **obligatoria** el método **POST**.

Nota: **GET** y **POST** son verbos del protocolo [HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Methods).

En este caso la respuesta que enviará la clase al llamar a la página a traves del método **GET** será el texto **'Hola mundo HTML y Python!'**.

````python
class Index:
    def GET(self):
        return 'Hola mundo HTML y Python!'
````

## 6. Inicializar la aplicación

Al ejecutar el archivo directamente con **python3 app.py** se llama al método run **app.run()** inicia el servidor web **Cherrypy**.

````python
if __name__ == "__main__":
    app.run()
````

## 7. Funcionamiento del servidor

Una vez iniciado el servidor, se puede acceder a la aplicación web a través de un navegador web utilizando la URL proporcionada por el servidor.

La URL **http://0.0.0.0:8080/** indica que el servidor está escuchando en todas las interfaces de red disponibles en el puerto 8080, la IP es asignada por el sistema operativo o el contenedor donde se ejecuta la aplicación.

````shell
http://0.0.0.0:8080/

````
## 8. Servidor en funcionamiento respondiendo peticiones

Cuando se accede a la URL desde un navegador, el servidor web responde con el contenido de la página solicitada. En este caso, al acceder a la ruta raíz **/**, se recibe el mensaje **'Hola mundo HTML y Python!'**.

NOTA: la respuesta del servidor [cherrypy](https://webpy.org/cookbook/ssl) es un texto plano, no es un HTML.

````shell
127.0.0.1:51186 - - [29/May/2025 19:24:46] "HTTP/1.1 GET /" - 200 OK
````

## 9. Detener el servidor

Para detener el servidor, se puede utilizar la combinación de teclas **Ctrl + C** en la terminal donde se está ejecutando la aplicación. 

