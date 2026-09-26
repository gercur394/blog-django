# Blog Django

Proyecto de un blog web desarrollado con Django. Permite crear, ver, editar y eliminar publicaciones (CRUD completo) desde el propio sitio, incluyendo carga de imágenes para cada post.

## Descripción

Este repositorio contiene un proyecto Django con una aplicación llamada `posts`. Además de las páginas de inicio, "Acerca de" y listado, el sitio permite gestionar publicaciones completas desde la interfaz web: crearlas, verlas en detalle, editarlas y eliminarlas (con confirmación previa), todo con soporte para imágenes.

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

## Operaciones CRUD disponibles

- **Listar** (`/posts/`): muestra las publicaciones con estado "publicado", ordenadas de la más reciente a la más antigua.
- **Ver detalle** (`/posts/<slug>/`): muestra título, contenido, autor, estado, fecha y la imagen del post (si tiene una cargada).
- **Crear** (`/posts/crear/`): formulario para cargar un nuevo post, incluyendo una imagen opcional.
- **Editar** (`/posts/<slug>/editar/`): formulario precargado con los datos del post, permite modificar cualquier campo, incluida la imagen.
- **Eliminar** (`/posts/<slug>/eliminar/`): muestra una página de confirmación antes de borrar el post definitivamente.

Cada post se identifica en la URL mediante un **slug**, generado automáticamente a partir del título la primera vez que se guarda.

## Manejo de imágenes

- El modelo `Post` incluye un campo `imagen` (`ImageField`), opcional, que guarda los archivos subidos dentro de la carpeta `media/posts/`.
- Se utiliza la librería **Pillow** para que Django pueda procesar archivos de imagen.
- En `settings.py` se configuraron `MEDIA_URL` y `MEDIA_ROOT` para definir dónde se guardan las imágenes y desde qué dirección se sirven.
- En `blog_project/urls.py` se agregó la configuración para servir esos archivos durante el desarrollo (solo cuando `DEBUG = True`).
- El formulario de creación/edición (`post_form.html`) incluye el atributo `enctype="multipart/form-data"`, necesario para que los archivos viajen correctamente al servidor; las vistas de crear y editar procesan `request.FILES` junto con `request.POST`.

### Cómo probar la carga de imágenes

1. Ingresar a `/posts/crear/` o editar un post existente.
2. En el campo de imagen del formulario, seleccionar un archivo desde la computadora.
3. Guardar el formulario.
4. Entrar al detalle del post (`/posts/<slug>/`): la imagen cargada debe visualizarse debajo de los datos del post. Si el post no tiene imagen asociada, esa sección simplemente no se muestra.

## Configuración

- Idioma: español (`es-ar`)
- Zona horaria: `America/Argentina/Buenos_Aires`

## Aplicaciones

- **posts**: aplicación principal del blog. Incluye el modelo `Post` (título, contenido, autor, fecha de creación, estado, imagen y slug), su registro en el panel admin, el formulario `PostForm`, y las vistas de inicio, "Acerca de", listado y CRUD completo de publicaciones.

## Páginas del sitio

- `/` — Inicio
- `/posts/` — Listado de publicaciones
- `/posts/crear/` — Crear un nuevo post
- `/posts/<slug>/` — Detalle de un post
- `/posts/<slug>/editar/` — Editar un post
- `/posts/<slug>/eliminar/` — Confirmar eliminación de un post
- `/acerca/` — Acerca de
- `/admin/` — Panel de administración