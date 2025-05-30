# 4. Uso de templates HTML y listas de datos en web.py

## 1. Ejemplo: Templates y envío de datos

El siguiente ejemplo muestra cómo utilizar templates **HTML** y enviar datos desde Python usando [web.py Templator](https://webpy.org/docs/0.3/templetor).

Se desarrollan dos páginas web (**index.html** y **clientes.html**) y sus respectivas clases (**Index** y **Clientes**).

```python
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
```

## 2. Páginas web y templates

Este ejemplo contiene dos páginas web: **index.html** y **clientes.html**.

### 2.1 index.html

Esta página utiliza **$def with(message)** en la primera línea, lo que permite recibir cualquier objeto enviado desde Python con **web.py**.

> **Nota:** El nombre de la variable (`message`) puede ser cualquiera, se recomienda que coincida con el parámetro enviado desde Python.

```html
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
```

### 2.2 clientes.html

De forma similar, **$def with(nombres)** permite recibir una lista de nombres desde Python.

```html
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
```

Para mostrar cada valor recibido, se utiliza un **bucle for** dentro del template, igual que en una aplicación de consola. Así, se combinan etiquetas **HTML** y **código Python** para mostrar los datos en una lista no numerada:

```python
<ul>
    $for nombre in nombres:
        <li>${nombre}</li>
</ul>
```

## 3. Renderizado de páginas recibiendo datos

En el caso de **index**, se envía una variable global `self.message` (tipo `str`) al template:

```python
class Index:
    def __init__(self):
        self.message = "Página de inicio"

    def GET(self):
        return render.index(self.message)
```

En el caso de **clientes**, se envía una lista de nombres a través de la variable global `self.nombres_clientes`:

```python
class Clientes:
    def __init__(self):
        self.nombres_clientes = ["Dejah Thoris", "John Carter", "Carthoris", "Tars Tarkas"]

    def GET(self):
        return render.clientes(self.nombres_clientes)
```

> **Nota:** El proceso para enviar datos a los templates HTML es el mismo en ambos casos: se pasan como argumentos al llamar al template desde Python.

---

**Recomendaciones:**
- Usa nombres de variables descriptivos y consistentes entre Python y los templates.
- Separa claramente el código Python y el HTML para facilitar el mantenimiento.
- Agrega comentarios en el código para explicar la lógica principal.