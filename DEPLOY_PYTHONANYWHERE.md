# 🚀 Guía Completa: Deploy en PythonAnywhere

## 📋 Requisitos Previos

✅ Proyecto Django funcionando localmente
✅ Base de datos Supabase configurada
✅ Repositorio en GitHub (ya lo tienes: JuanMero2002/hackaton-prueba)
✅ Cuenta en PythonAnywhere (gratis)

---

## 🎯 PASO 1: Crear cuenta en PythonAnywhere

1. Ve a: https://www.pythonanywhere.com
2. Haz clic en **"Start running Python online in less than a minute!"**
3. Crea una cuenta **GRATUITA** (Beginner Account)
   - Username: Elige tu nombre de usuario
   - Email: Tu correo
   - Password: Una contraseña segura
4. Confirma tu email
5. Inicia sesión

---

## 🎯 PASO 2: Preparar tu repositorio GitHub

### 2.1. Verificar que `.env` NO esté en GitHub

```bash
# El archivo .env NO debe estar en GitHub (ya está en .gitignore)
# Verifica que .gitignore contenga:
.env
.env.local
*.env
```

### 2.2. Asegurar que requirements.txt esté actualizado

Tu `requirements.txt` debe tener:
```
Django==5.2.7
django-crispy-forms==2.3
crispy-bootstrap5==2024.10
Pillow==10.4.0
psycopg2-binary==2.9.9
supabase==2.11.0
python-decouple==3.8
```

### 2.3. Subir cambios a GitHub

```powershell
git add .
git commit -m "Preparando para deploy en PythonAnywhere"
git push origin main
```

---

## 🎯 PASO 3: Configurar PythonAnywhere

### 3.1. Abrir consola Bash

1. En el dashboard de PythonAnywhere
2. Ve a **"Consoles"** (en el menú superior)
3. Haz clic en **"Bash"** (o **"$ Bash"**)

### 3.2. Clonar tu repositorio

En la consola Bash, ejecuta:

```bash
# Clonar tu repositorio
git clone https://github.com/JuanMero2002/hackaton-prueba.git

# Entrar al directorio
cd hackaton-prueba

# Ver los archivos
ls -la
```

### 3.3. Crear entorno virtual

```bash
# Crear virtual environment con Python 3.10
mkvirtualenv --python=/usr/bin/python3.10 hackaton-env

# Debería decir: (hackaton-env) en el prompt
```

### 3.4. Instalar dependencias

```bash
# Activar el entorno (si no está activo)
workon hackaton-env

# Instalar dependencias
pip install -r requirements.txt

# Verificar que se instaló todo
pip list
```

---

## 🎯 PASO 4: Configurar variables de entorno

### 4.1. Crear archivo .env en PythonAnywhere

```bash
# Crear el archivo .env
nano .env
```

### 4.2. Pegar tus credenciales

Copia y pega esto (con TUS datos reales):

```env
# SUPABASE
SUPABASE_URL=https://owrgthzfdlnhkiwzdgbd.supabase.co
SUPABASE_KEY=your_supabase_anon_key_here

# POSTGRESQL
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=Milxi26.
DB_HOST=db.owrgthzfdlnhkiwzdgbd.supabase.co
DB_PORT=5432

# DJANGO
SECRET_KEY=django-insecure-^o$qnv_*2$h_j6+9ci7+i2%d1r+k!#$j_#967*caq9%id-x9*0
DEBUG=False
ALLOWED_HOSTS=tuusuario.pythonanywhere.com,localhost,127.0.0.1
```

**Guardar con:**
- `Ctrl + O` (Write Out)
- `Enter` (confirmar)
- `Ctrl + X` (Exit)

### 4.3. Verificar que se creó

```bash
cat .env
```

---

## 🎯 PASO 5: Configurar Django para producción

### 5.1. Crear archivo de configuración adicional

```bash
nano sistema_practicas/production_settings.py
```

Pegar esto:

```python
from .settings import *

# Configuración de producción
DEBUG = False

# Static files en PythonAnywhere
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Security
SECURE_SSL_REDIRECT = False  # PythonAnywhere maneja SSL
SESSION_COOKIE_SECURE = False  # Cambiar a True si usas HTTPS
CSRF_COOKIE_SECURE = False     # Cambiar a True si usas HTTPS
```

Guardar con `Ctrl+O`, `Enter`, `Ctrl+X`

### 5.2. Recolectar archivos estáticos

```bash
# Asegúrate de estar en el directorio del proyecto
cd ~/hackaton-prueba

# Activar entorno
workon hackaton-env

# Recolectar estáticos
python manage.py collectstatic --noinput
```

### 5.3. Verificar migraciones

```bash
python manage.py migrate
```

---

## 🎯 PASO 6: Configurar Web App en PythonAnywhere

### 6.1. Crear Web App

1. Ve a la pestaña **"Web"** (en el menú superior)
2. Haz clic en **"Add a new web app"**
3. Haz clic en **"Next"**
4. Selecciona **"Manual configuration"** (NO usar wizard)
5. Selecciona **"Python 3.10"**
6. Haz clic en **"Next"**

### 6.2. Configurar el código

En la sección **"Code"**:

**Source code:**
```
/home/TUUSUARIO/hackaton-prueba
```

**Working directory:**
```
/home/TUUSUARIO/hackaton-prueba
```

### 6.3. Configurar Virtual Environment

En la sección **"Virtualenv"**:

```
/home/TUUSUARIO/.virtualenvs/hackaton-env
```

---

## 🎯 PASO 7: Configurar WSGI

### 7.1. Editar archivo WSGI

1. En la pestaña **"Web"**, busca la sección **"Code"**
2. Haz clic en el enlace del archivo WSGI (algo como `/var/www/tuusuario_pythonanywhere_com_wsgi.py`)
3. **BORRA TODO** el contenido
4. Pega esto:

```python
import os
import sys

# Añadir el directorio del proyecto al path
path = '/home/TUUSUARIO/hackaton-prueba'  # CAMBIA TUUSUARIO
if path not in sys.path:
    sys.path.insert(0, path)

# Cargar variables de entorno desde .env
from dotenv import load_dotenv
project_folder = os.path.expanduser('~/hackaton-prueba')
load_dotenv(os.path.join(project_folder, '.env'))

# Configurar Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'sistema_practicas.settings'

# Cargar la aplicación WSGI de Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**IMPORTANTE**: Reemplaza `TUUSUARIO` con tu nombre de usuario de PythonAnywhere

5. Haz clic en **"Save"**

---

## 🎯 PASO 8: Configurar archivos estáticos

En la pestaña **"Web"**, sección **"Static files"**:

### 8.1. Agregar ruta de static

- **URL:** `/static/`
- **Directory:** `/home/TUUSUARIO/hackaton-prueba/staticfiles`

### 8.2. Agregar ruta de media

- **URL:** `/media/`
- **Directory:** `/home/TUUSUARIO/hackaton-prueba/media`

---

## 🎯 PASO 9: Instalar python-dotenv

```bash
# En la consola Bash
workon hackaton-env
pip install python-dotenv
```

Y agregar a `requirements.txt`:
```bash
echo "python-dotenv==1.0.0" >> requirements.txt
```

---

## 🎯 PASO 10: Actualizar settings.py para producción

Volver a la consola y editar settings.py:

```bash
nano sistema_practicas/settings.py
```

Buscar la línea `ALLOWED_HOSTS` y cambiar a:

```python
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')
```

Guardar con `Ctrl+O`, `Enter`, `Ctrl+X`

---

## 🎯 PASO 11: Reload y Verificar

### 11.1. Recargar la aplicación

1. En la pestaña **"Web"**
2. Haz clic en el botón verde **"Reload TUUSUARIO.pythonanywhere.com"**

### 11.2. Ver tu aplicación

Haz clic en el enlace: `https://TUUSUARIO.pythonanywhere.com`

---

## 🎯 PASO 12: Verificar logs (si hay errores)

Si algo no funciona:

1. En la pestaña **"Web"**
2. Baja hasta **"Log files"**
3. Revisa:
   - **Error log** → Errores de la aplicación
   - **Server log** → Errores del servidor

---

## 🐛 SOLUCIÓN DE PROBLEMAS COMUNES

### Error: "DisallowedHost"
✅ Verifica `ALLOWED_HOSTS` en `.env`:
```env
ALLOWED_HOSTS=tuusuario.pythonanywhere.com,localhost,127.0.0.1
```

### Error: "No module named 'psycopg2'"
✅ Instala en el entorno virtual:
```bash
workon hackaton-env
pip install psycopg2-binary
```

### Error: "Could not connect to database"
✅ Verifica las credenciales de Supabase en `.env`
✅ Asegúrate de que Supabase permite conexiones externas

### Error: "Static files not found"
✅ Ejecuta:
```bash
python manage.py collectstatic --noinput
```
✅ Verifica la configuración de static files en la pestaña Web

### Error: "500 Internal Server Error"
✅ Revisa el error log en la pestaña Web
✅ Verifica que `DEBUG=False` en `.env`
✅ Asegúrate de que `SECRET_KEY` esté configurado

---

## 🔄 ACTUALIZAR LA APLICACIÓN

Cada vez que hagas cambios:

```bash
# 1. En tu computadora local, subir a GitHub
git add .
git commit -m "Descripción de cambios"
git push origin main

# 2. En PythonAnywhere, en la consola Bash
cd ~/hackaton-prueba
git pull origin main

# 3. Si hay nuevas dependencias
workon hackaton-env
pip install -r requirements.txt

# 4. Si hay migraciones
python manage.py migrate

# 5. Si hay nuevos archivos estáticos
python manage.py collectstatic --noinput

# 6. Recargar la web app
# Ve a la pestaña Web y haz clic en Reload
```

---

## 📊 LIMITACIONES DEL PLAN GRATUITO

- ⏰ **Uptime**: La aplicación duerme después de 3 meses sin visitas
- 🗄️ **Almacenamiento**: 512 MB
- 🔄 **CPU**: 100 segundos/día
- 🌐 **Dominio**: `tuusuario.pythonanywhere.com`
- 📅 **Renovación**: Debes renovar cada 3 meses (gratis)

Para más recursos, necesitas el plan **Hacker** ($5/mes)

---

## ✅ CHECKLIST FINAL

Antes de considerar el deploy completo:

- [ ] Aplicación accesible en `https://tuusuario.pythonanywhere.com`
- [ ] Panel admin funciona (`/admin`)
- [ ] Archivos estáticos cargan correctamente
- [ ] Chatbot funciona
- [ ] Base de datos Supabase conectada
- [ ] Registro de estudiantes funciona
- [ ] Registro de empresas funciona
- [ ] Sin errores en el error log

---

## 🎉 ¡FELICIDADES!

Tu aplicación Django con Supabase está desplegada en PythonAnywhere.

**URL de tu aplicación**: `https://TUUSUARIO.pythonanywhere.com`

¡Comparte el enlace y prueba todas las funcionalidades! 🚀
