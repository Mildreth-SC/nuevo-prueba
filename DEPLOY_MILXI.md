# 🚀 Deploy en PythonAnywhere - Comandos para Milxi

## ✅ INFORMACIÓN
- **Usuario PythonAnywhere:** Milxi
- **URL final:** https://milxi.pythonanywhere.com
- **Repositorio:** https://github.com/Mildreth-SC/nuevo-prueba

---

## PASO 1: ABRIR BASH CONSOLE

1. Ve a: https://www.pythonanywhere.com/user/Milxi/
2. Dashboard → **Consoles**
3. Click en **"Bash"**

---

## PASO 2: CLONAR REPOSITORIO

Copia y pega estos comandos UNO POR UNO:

```bash
cd ~
git clone https://github.com/Mildreth-SC/nuevo-prueba.git
cd nuevo-prueba
ls -la
```

Deberías ver todos tus archivos listados.

---

## PASO 3: CREAR ENTORNO VIRTUAL E INSTALAR DEPENDENCIAS

```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
```

Espera a que termine, luego:

```bash
pip install -r requirements.txt
```

⏱️ Esto tomará 2-3 minutos. Espera a que termine.

---

## PASO 4: CREAR ARCHIVO .env

```bash
nano .env
```

Copia y pega EXACTAMENTE esto:

```env
# Django
SECRET_KEY=django-insecure-7cj+9fy6a^n3_i8z2k&x*y7(v)#gf+s@4r$q^2h-7&d*+1
DEBUG=False
ALLOWED_HOSTS=milxi.pythonanywhere.com

# Supabase Database
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=Milxi26.
DB_HOST=db.owrgthzfdlnhkiwzdgbd.supabase.co
DB_PORT=5432

# Supabase API
SUPABASE_URL=https://owrgthzfdlnhkiwzdgbd.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im93cmd0aHpmZGxuaGtpd3pkZ2JkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzA0Njk4MTYsImV4cCI6MjA0NjA0NTgxNn0.K7X3qCjYZ8QnN5fGX6kGTXV7yHVqZXhI5pQrLmNjK4Y
```

Para guardar:
1. Presiona **Ctrl + X**
2. Presiona **Y**
3. Presiona **Enter**

---

## PASO 5: VERIFICAR CONEXIÓN

```bash
python manage.py check
```

Debe decir: **"System check identified no issues"**

---

## PASO 6: RECOLECTAR ARCHIVOS ESTÁTICOS

```bash
python manage.py collectstatic --noinput
```

---

## PASO 7: CREAR WEB APP

1. Ve a la pestaña **"Web"** en el Dashboard
2. Click en **"Add a new web app"**
3. Click **"Next"** (acepta el dominio milxi.pythonanywhere.com)
4. Selecciona **"Manual configuration"**
5. Selecciona **"Python 3.10"**
6. Click **"Next"**

---

## PASO 8: CONFIGURAR VIRTUALENV

En la sección **"Virtualenv"**, pega esto:

```
/home/Milxi/.virtualenvs/myenv
```

Click en el ✓ (check) para guardar.

---

## PASO 9: CONFIGURAR WSGI

1. Click en el link del **"WSGI configuration file"**
2. **BORRA TODO** el contenido
3. Copia y pega esto:

```python
import os
import sys

# Agregar proyecto al path
path = '/home/Milxi/nuevo-prueba'
if path not in sys.path:
    sys.path.append(path)

# Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'sistema_practicas.settings'

# Cargar variables de entorno
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('/home/Milxi/nuevo-prueba/.env')
load_dotenv(dotenv_path=env_path)

# Django WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

4. Click **"Save"** (arriba a la derecha)

---

## PASO 10: CONFIGURAR ARCHIVOS ESTÁTICOS

Vuelve a la pestaña **"Web"**.

En la sección **"Static files"**, click en **"Enter path"** y agrega:

### Primera entrada:
- **URL:** `/static/`
- **Directory:** `/home/Milxi/nuevo-prueba/staticfiles/`

### Segunda entrada:
- **URL:** `/media/`
- **Directory:** `/home/Milxi/nuevo-prueba/media/`

---

## PASO 11: RECARGAR LA WEB APP

1. Scroll hasta arriba
2. Click en el botón verde **"Reload milxi.pythonanywhere.com"**
3. Espera 10 segundos

---

## PASO 12: ¡PROBAR!

Abre en tu navegador:
```
https://milxi.pythonanywhere.com
```

¡Debe estar funcionando! 🎉

---

## 🔐 CREDENCIALES PARA PROBAR

**Estudiante:**
- Usuario: `est1312345678`
- Contraseña: `estudiante123`
- URL: https://milxi.pythonanywhere.com

**Empresa:**
- Usuario: `techsolutions_ecuador`
- Contraseña: `empresa123`

**Admin:**
- Usuario: `Mildreth`
- Contraseña: (la que configuraste)
- URL: https://milxi.pythonanywhere.com/admin

---

## 🆘 SI HAY ERRORES

En la consola Bash:

```bash
tail -f /var/log/Milxi.pythonanywhere.com.error.log
```

Presiona **Ctrl + C** para salir.

---

## ✅ RESUMEN

1. ✅ Bash console → clonar repo
2. ✅ Crear virtualenv e instalar dependencias
3. ✅ Crear archivo .env
4. ✅ Verificar con `python manage.py check`
5. ✅ Collectstatic
6. ✅ Crear Web App
7. ✅ Configurar virtualenv
8. ✅ Configurar WSGI
9. ✅ Configurar static files
10. ✅ Reload
11. ✅ ¡Funciona!

**Tiempo total: 15-20 minutos**

---

**¡Sigue estos pasos en orden y tu aplicación estará online!** 🚀

Si tienes algún error, dime en qué paso estás y te ayudo.
