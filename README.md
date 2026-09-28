# Blog Django

Proyecto de un blog web desarrollado con Django. Permite crear, ver, editar y eliminar publicaciones (CRUD completo) con imágenes, y ahora incluye un sistema de usuarios: registro, inicio y cierre de sesión, y perfiles con biografía y avatar.

## Descripción

Este repositorio contiene un proyecto Django con dos aplicaciones: `posts` (publicaciones del blog) y `accounts` (usuarios y perfiles). Los visitantes anónimos pueden ver el listado y el detalle de los posts publicados, pero crear, editar o eliminar publicaciones requiere estar autenticado. Cada usuario registrado tiene un perfil propio, con biografía, link web y avatar.

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

Instalar dependencias (incluye Django y Pillow, necesaria para trabajar con imágenes):

```bash
pip install -r requirements.txt
```

Aplicar las migraciones (crea la base de datos local, incluyendo la tabla de perfiles):

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

## Sistema de usuarios

### Registro

Cualquier visitante puede crear una cuenta nueva en `/accounts/registro/`, completando usuario, email y contraseña. Al registrarse, además del usuario se crea automáticamente su perfil asociado (inicialmente vacío), y se redirige a la página de login.

### Iniciar sesión

Un usuario ya registrado puede iniciar sesión en `/accounts/login/`. Al loguearse correctamente, es redirigido al listado de posts.

### Cerrar sesión

El cierre de sesión se realiza mediante el botón "Cerrar sesión" del menú (no funciona escribiendo la URL directamente en el navegador, ya que por seguridad solo acepta la acción desde el formulario del sitio). Al cerrar sesión, se redirige al listado de posts.

### Perfil

Cada usuario autenticado puede ver su perfil en `/accounts/perfil/` (biografía, sitio web y avatar) y editarlo en `/accounts/perfil/editar/`. La edición permite modificar biografía, link web y subir/cambiar el avatar. Estas páginas requieren estar logueado.

El modelo `Perfil` (en `accounts/models.py`) se relaciona con el modelo `User` de Django mediante un `OneToOneField`, es decir, cada usuario tiene exactamente un perfil.

## Manejo de avatares

- El campo `avatar` del modelo `Perfil` es un `ImageField`, opcional, que guarda las imágenes dentro de `media/avatares/` (separado de `media/posts/`, donde se guardan las imágenes de las publicaciones).
- Usa la misma configuración de `MEDIA_URL` y `MEDIA_ROOT` definida en `settings.py`, y el mismo mecanismo de `request.FILES` para procesar el archivo subido en el formulario de edición de perfil.
- En la página de perfil, el avatar solo se muestra si el usuario tiene uno cargado; si no, esa sección simplemente no aparece.

## Rutas protegidas

Requieren estar autenticado (usan el decorador `@login_required`, que redirige al login si no hay sesión iniciada):

- `/posts/crear/` — crear un post
- `/posts/<slug>/editar/` — editar un post
- `/posts/<slug>/eliminar/` — eliminar un post
- `/accounts/perfil/` — ver el propio perfil
- `/accounts/perfil/editar/` — editar el propio perfil

Siguen siendo públicas (visibles sin necesidad de iniciar sesión):

- `/` — Inicio
- `/posts/` — Listado de publicaciones
- `/posts/<slug>/` — Detalle de un post
- `/acerca/` — Acerca de

## Configuración

- Idioma: español (`es-ar`)
- Zona horaria: `America/Argentina/Buenos_Aires`
- `LOGIN_URL`, `LOGIN_REDIRECT_URL` y `LOGOUT_REDIRECT_URL` configurados en `settings.py`

## Aplicaciones

- **posts**: modelo `Post` (título, contenido, autor, fecha, estado, imagen, slug), formulario `PostForm`, vistas de inicio, "Acerca de", listado y CRUD de publicaciones (protegido salvo listado/detalle).
- **accounts**: modelo `Perfil` (relacionado con `User`, con biografía, link web y avatar), formularios de registro (`RegistroForm`) y edición de perfil (`PerfilForm`), vistas de registro, ver perfil y editar perfil, y las rutas de login/logout provistas por Django.

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