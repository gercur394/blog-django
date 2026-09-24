# Blog Django

Proyecto de un blog web desarrollado con Django, con publicaciones gestionadas desde una base de datos real a través del panel administrativo.

## Descripción

Este repositorio contiene un proyecto Django con una aplicación llamada `posts`. El sitio cuenta con página de inicio, página "Acerca de" y una página de listado de publicaciones (`/posts/`) que muestra dinámicamente los posts cargados desde el panel de administración, consultados mediante el ORM de Django.

## Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar a la carpeta del proyecto:

```bash
cd NOMBRE_DEL_REPOSITORIO
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual:

En Windows con Git Bash:

```bash
source venv/Scripts/activate
```

En Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Aplicar las migraciones (crea la base de datos local):

```bash
python manage.py migrate
```

Crear un superusuario para acceder al panel administrativo:

```bash
python manage.py createsuperuser
```

Ejecutar el servidor:

```bash
python manage.py runserver
```

Abrir en el navegador:

```
http://127.0.0.1:8000/
```

## Panel de administración

El panel admin permite cargar, editar y eliminar publicaciones sin escribir código.

1. Con el servidor corriendo, ingresar a:

```
http://127.0.0.1:8000/admin/
```

2. Iniciar sesión con el superusuario creado en la instalación.
3. Ingresar a la sección **Posts** y usar **Add Post** para cargar una nueva publicación (título, contenido, autor y estado).
4. Las publicaciones con estado `publicado` aparecen automáticamente en la página `/posts/` del sitio.

## Configuración

- Idioma: español (`es-ar`)
- Zona horaria: `America/Argentina/Buenos_Aires`

## Aplicaciones

- **posts**: aplicación principal del blog. Incluye el modelo `Post` (título, contenido, autor, fecha de creación y estado), su registro en el panel admin, y las vistas de inicio, "Acerca de" y listado de publicaciones.

## Páginas del sitio

- `/` — Inicio
- `/posts/` — Listado de publicaciones (posts con estado "publicado", ordenados por fecha de creación descendente)
- `/acerca/` — Acerca de
- `/admin/` — Panel de administración