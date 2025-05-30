# 3. Templates html y lista de datos

## 1. Ejemplo de templates y lista de datos

El siguiente código muestra el uso de templates **HTML** y datos enviados a los archivos desde python [web.py Templator](https://webpy.org/docs/0.3/templetor).

Este ejemplo muestra la forma de desarrollar 2 paginas web (**index.html** y **clientes.html**) con sus respectivas clases (**Index** y **Clientes**).

````python
import web

urls = (
    '/', 'Index',
    '/clientes', 'Clientes',
)
render = web.template.render('templates')
app = web.application(urls, globals())

class Index:

    def __init__(self):
        self.message = "Página de inicio"


    def GET(self):
        return render.index(self.message)


class Clientes:

    def __init__(self):
        self.nombres_clientes = ["Dejah Thoris", "John Carter", "Carthoris", "Tars Tarkas"]


    def GET(self):
        return render.clientes(self.nombres_clientes)


if __name__ == "__main__":
    app.run()
````

## 2. Páginas web

Este ejemplo contiene dos paginas web **index.html** y **clientes.html**.

### 2.1 index.html

Está página es una extensión del ejemplo anterior, como primer línea se utiliza **$def with(message)** lo que permite recibir cualquier tipo de objeto enviado desde **python** con **web.py**.

**NOTA**: El objeto **message** puede tener cualquier nombre.


````html
$def with(message)
<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Variables</title>
    </head>
    <body>
        <h1>$message</h1>
        <a href="/clientes">Ver clientes</a>
    </body>
</html>
````

### 2.2 clientes.html

Tal cómo se menciono anteriormente **$def with(nombres)** puede recibir casi cualquier tipo de objeto, en este caso recibe una lista con 4 elementos.

````html
$def with(nombres)
<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Variables</title>
    </head>
    <body>
        <h1>Lista de clientes</h1> 
        <a href="/">Volver al inicio</a>
        <ul>
            $for nombre in nombres:
                <li>${nombre}</li>
        </ul>
    </body>
</html>
````

Para mostrar cada uno de los valores recibidos se utiliza un **bucle for**, tal como se haría en una aplicación de consola.

Aquí se puede apreciar cómo se estan utilizando etiquetas de **html** y **código de python** para mostrar cada valor recibido en una lista NO numerada **<ul>**.

````python
<ul>
    $for nombre in nombres:
        <li>${nombre}</li>
</ul>
````

## 3. Renderizado de paginas recibiendo datos

En el caso de **index** se esta enviando una variable global **self.message** que contiene un str.

````python
class Index:

    def __init__(self):
        self.message = "Página de inicio"


    def GET(self):
        return render.index(self.message)
````

En el caso de **clientes** se esta enviando una variable global **self.nombre_clientes** que contiene una lista de nombres.

**NOTA**: el proceso para enviar los datos a las paginas html en ambos casos es el mismo, es decir se agregan como un parámetro dentro de los paréntisis.

````python
class Clientes:

    def __init__(self):
        self.nombres_clientes = ["Dejah Thoris", "John Carter", "Carthoris", "Tars Tarkas"]


    def GET(self):
        return render.clientes(self.nombres_clientes)
````