# Introducción a Web.py y Python

Este repositorio contiene ejercicios prácticos para aprender el uso de web.py y la integración de HTML en aplicaciones Python.

## 1. Crear el archivo **.gitignore**

Crea el archivo **.gitignore** para especificar los archivos y carpetas que no deben sincronizarse con el repositorio.

````shell
*.pyc
__pycache__/
.venv/
````

## 2. Crear el entorno virtual (**virtual environment**)

Crea un entorno virtual de Python para aislar las dependencias del proyecto.

````shell
python3 -m venv .venv
````

## 3. Activar el entorno virtual

Activa el entorno virtual para instalar las librerías necesarias para el proyecto.

````shell
source .venv/bin/activate
````

## 4. Actualizar **pip** dentro del entorno virtual

Actualiza la versión de **pip** para poder instalar las últimas versiones de las librerías.

````shell
pip install --upgrade pip
````

## 5. Verificar las librerías instaladas

Verifica qué librerías y versiones tienes instaladas en el entorno virtual.

````shell
pip freeze
````

## 6. Instalar librerías necesarias

Instala las librerías requeridas para el proyecto. Por ejemplo, para este repositorio:

````shell
pip install web.py
````

## 7. Crear el archivo **requirements.txt**

Genera el archivo **requirements.txt** con las librerías y versiones utilizadas en el proyecto.

````shell
pip freeze > requirements.txt
````

## 8. Crear el archivo **runtime.txt**

Crea el archivo **runtime.txt** con la versión de Python utilizada en el proyecto.

````shell
python3 -V > runtime.txt
````

## 9. Indexar los archivos creados con **git**

Agrega los archivos y cambios realizados al control de versiones con **git**.

````shell
git add .
````

## 10. Generar un **commit**

Realiza un **commit** con un mensaje descriptivo sobre los cambios realizados.

````shell
git commit -m "CREATED configuracion basica"
````

## 11. Realizar un **push** 

Sube los cambios realizados al repositorio de **GitHub**.

````shell
git push -u origin main
````

---

**Notas y recomendaciones:**
- Asegúrate de activar el entorno virtual cada vez que trabajes en el proyecto.
- El archivo **.gitignore** es fundamental para evitar subir archivos innecesarios o sensibles.
- Utiliza mensajes de commit claros y descriptivos para facilitar el seguimiento de los cambios.


