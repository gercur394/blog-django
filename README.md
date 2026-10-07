# Blog Django

Blog web desarrollado con Django, con gestión completa de publicaciones (incluyendo imágenes) y un sistema de usuarios con registro, autenticación y perfiles.

## Descripción

Este proyecto es un blog donde los visitantes pueden leer las publicaciones sin necesidad de registrarse, mientras que los usuarios autenticados pueden crear, editar y eliminar posts, además de gestionar su propio perfil con biografía, sitio web y avatar. Fue desarrollado de forma incremental a lo largo de un curso, partiendo de un script simple en consola hasta llegar a esta aplicación web completa.

## Tecnologías utilizadas

- Python
- Django
- SQLite (base de datos de desarrollo)
- Pillow (procesamiento de imágenes)
- HTML / CSS

## Funcionalidades principales

- **Publicaciones (CRUD completo desde la interfaz web)**: listar, ver detalle, crear, editar y eliminar posts, con carga de imagen opcional por publicación.
- **Usuarios**: registro, inicio de sesión y cierre de sesión.
- **Perfiles**: cada usuario tiene un perfil con biografía, link web y avatar, que puede ver y editar.
- **Rutas protegidas**: crear, editar y eliminar posts, así como editar el perfil, requieren tener una sesión iniciada (protegido a nivel de vista con `@login_required`, no solo ocultando botones en el template).
- **Navegación según el usuario**: el menú muestra opciones distintas según haya o no una sesión iniciada.

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

Aplicar las migraciones (crea la base de datos local, incluyendo las tablas de posts y perfiles):

```bash
python manage.py migrate
```

Crear un superusuario (necesario para acceder al panel `/admin/` y para poder iniciar sesión y probar el sitio como usuario autenticado):

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

## Probar el proyecto desde cero

Este repositorio no incluye `db.sqlite3` ni la carpeta `media/` (se generan localmente y están excluidos mediante `.gitignore`). Para tener contenido de prueba después de instalar el proyecto:

1. Seguir los pasos de instalación de arriba hasta tener el servidor corriendo.
2. Crear una cuenta nueva en `/accounts/registro/`, o usar el superusuario creado en la instalación para iniciar sesión en `/accounts/login/`.
3. Ir a `/posts/crear/` y cargar algunas publicaciones de prueba (con o sin imagen).
4. Opcionalmente, entrar a `/admin/` con el superusuario para revisar o administrar los posts y perfiles cargados.

## Rutas protegidas

Requieren tener una sesión iniciada:

- `/posts/crear/` — crear un post
- `/posts/<slug>/editar/` — editar un post
- `/posts/<slug>/eliminar/` — eliminar un post
- `/accounts/perfil/` — ver el propio perfil
- `/accounts/perfil/editar/` — editar el propio perfil

Son públicas (accesibles sin iniciar sesión):

- `/` — Inicio
- `/posts/` — Listado de publicaciones
- `/posts/<slug>/` — Detalle de un post
- `/acerca/` — Acerca de

## Páginas del sitio

- `/` — Inicio
- `/posts/` — Listado de publicaciones
- `/posts/crear/` — Crear un nuevo post (requiere login)
- `/posts/<slug>/` — Detalle de un post
- `/posts/<slug>/editar/` — Editar un post (requiere login)
- `/posts/<slug>/eliminar/` — Confirmar eliminación de un post (requiere login)
- `/acerca/` — Acerca de
- `/accounts/registro/` — Crear una cuenta
- `/accounts/login/` — Iniciar sesión
- `/accounts/logout/` — Cerrar sesión
- `/accounts/perfil/` — Ver mi perfil (requiere login)
- `/accounts/perfil/editar/` — Editar mi perfil (requiere login)
- `/admin/` — Panel de administración

## Autor

Germán Curbelo