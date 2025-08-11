# vistaControlador

## 🖥️ Descripción

Este proyecto implementa el patrón **Modelo‑Vista‑Controlador (MVC)** para una aplicación educativa o demostrativa. Su propósito es ilustrar cómo estructurar una aplicación dividiendo responsabilidades entre el Modelo (representación de datos) la Vista (interfaz de usuario) y el Controlador (flujo de interacción).

## 📦 Tecnologías utilizadas

- **Lenguaje principal:** Python
- **Entorno de desarrollo:** Django
- **Paradigma:** Arquitectura MVC
- **Dependencias externas:** Ninguna (proyecto simple para estudio)

## 📁 Estructura del proyecto
```
vistaControlador/
├── init.py       # Reconocimiento de proyecto como modulo de Python.
├── asgi.py       # Puntos de entrada para despliegue asincrónico de la aplicación.
├── settings.py   # Configuración del proyecto.
├── urls.py       # Clases que representan y manipulan datos
├── tests.py      # Funciones para pruebas unitarias
├── urls.py       # Sistema de ruteo del proyecto.
├── wsgi.py       # Puntos de entrada para despliegue tradicional  de la aplicación.

inventario/       # App inventario
├── migrations/   # Ubicación de migraciones de la app.
├── static/       # Archivos estáticos como CSS.
├── templates/    # Interfaces gráficas o salidas visuales
├── init.py       # Reconocimiento de inventario como modulo de Python.
├── admin.py      # Archivo de lógica para admin de Django.
├── apps.py       # Configuración de la app.
├── models.py     # Clases que representan y manipulan datos
├── tests.py      # Funciones para pruebas unitarias
├── urls.py       # Sistema de ruteo de la app.
├── views.py      # Clases que gestionan la lógica de flujo.

db.sqlite3        # Base de datos SQLite3
manage.py         # Archivo de comandos del proyecto

```
Cada elemento representa una capa del patrón MVC:

- `models.py`: contiene la lógica de datos y clases de negocio.
- `templates/`: contiene interfaces gráficas o representaciones visuales.
- `views.py`: maneja los eventos y coordina la comunicación entre vista y modelo.

## 🚀 Cómo usar este proyecto

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Nram94/modelo.git
   cd modelo


## 📄 Licencia
Este proyecto está bajo la licencia MIT.
Puedes utilizarlo, modificarlo y distribuirlo libremente.
Consulta el archivo LICENSE para más detalles.

👤 Autor
GitHub: Nram94
