# 🚀 Deploy PythonAnywhere - Guía Rápida

## ✅ Tu información de GitHub
- **Repositorio:** https://github.com/Mildreth-SC/nuevo-prueba
- **Usuario GitHub:** Mildreth-SC
- **Branch:** main

---

## 🔐 Credenciales de Supabase (para el .env)

```env
# Django
SECRET_KEY=django-insecure-7cj+9fy6a^n3_i8z2k&x*y7(v)#gf+s@4r$q^2h-7&d*+1
DEBUG=False
ALLOWED_HOSTS=tuusuario.pythonanywhere.com

# Supabase Database
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=Milxi26.
DB_HOST=db.owrgthzfdlnhkiwzdgbd.supabase.co
DB_PORT=5432

# Supabase API
SUPABASE_URL=https://owrgthzfdlnhkiwzdgbd.supabase.co
SUPABASE_KEY=(buscar en Supabase Dashboard → Settings → API → anon/public key)
```

**IMPORTANTE:** Reemplaza `tuusuario` con tu username de PythonAnywhere

---

## 📝 COMANDOS PARA BASH CONSOLE (Copiar y pegar)

### 1. Clonar repositorio
```bash
cd ~
git clone https://github.com/Mildreth-SC/nuevo-prueba.git
cd nuevo-prueba
```

### 2. Crear entorno virtual
```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
workon myenv
pip install -r requirements.txt
```

### 3. Crear archivo .env
```bash
nano .env
```
Pega el contenido de arriba (actualiza ALLOWED_HOSTS y SECRET_KEY si quieres)
- Guardar: `Ctrl + X`, luego `Y`, luego `Enter`

### 4. Verificar conexión a base de datos
```bash
python manage.py check
```

### 5. Recolectar archivos estáticos
```bash
python manage.py collectstatic --noinput
```

---

## 🌐 CONFIGURACIÓN WEB APP

### Crear Web App
1. Dashboard → Web tab
2. Add a new web app → Next
3. Manual configuration → Python 3.10

### Configurar Virtualenv
Ruta del virtualenv:
```
/home/tuusuario/.virtualenvs/myenv
```

### Configurar WSGI file
Reemplaza TODO el contenido con:

```python
import os
import sys

# Agregar proyecto al path
path = '/home/tuusuario/nuevo-prueba'
if path not in sys.path:
    sys.path.append(path)

# Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'sistema_practicas.settings'

# Cargar variables de entorno
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('/home/tuusuario/nuevo-prueba/.env')
load_dotenv(dotenv_path=env_path)

# Django WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**IMPORTANTE:** Reemplaza `tuusuario` con tu username en TODAS las líneas

### Configurar Static Files
| URL | Directory |
|-----|-----------|
| `/static/` | `/home/tuusuario/nuevo-prueba/staticfiles/` |
| `/media/` | `/home/tuusuario/nuevo-prueba/media/` |

---

## ✅ CHECKLIST DE DEPLOY

- [ ] Cuenta PythonAnywhere creada
- [ ] Bash console abierta
- [ ] Repositorio clonado
- [ ] Virtualenv creado
- [ ] Dependencias instaladas
- [ ] Archivo .env creado
- [ ] Web app configurada
- [ ] WSGI configurado
- [ ] Static files configurados
- [ ] Web app recargada
- [ ] Sitio funcionando

---

## 🎯 DESPUÉS DE CONFIGURAR TODO

1. Ve a la pestaña Web
2. Click en el botón verde **"Reload tuusuario.pythonanywhere.com"**
3. Visita: `https://tuusuario.pythonanywhere.com`
4. ¡Debe estar funcionando! 🎉

---

## 🔐 CREDENCIALES PARA PROBAR

**Estudiante:**
- Usuario: `est1312345678`
- Contraseña: `estudiante123`

**Empresa:**
- Usuario: `techsolutions_ecuador`
- Contraseña: `empresa123`

**Admin:**
- Usuario: `Mildreth`
- URL: `/admin`

---

## 🆘 SI HAY ERRORES

Ver logs:
```bash
tail -f /var/log/tuusuario.pythonanywhere.com.error.log
```

Presiona `Ctrl + C` para salir

---

**¡Sigue estos pasos y tu aplicación estará online en 15-20 minutos!** 🚀
