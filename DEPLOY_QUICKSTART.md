# 🚀 DEPLOY RÁPIDO - PythonAnywhere

## ⚡ Resumen en 5 pasos

### 1️⃣ Preparar GitHub
```powershell
git add .
git commit -m "Listo para deploy"
git push origin main
```

### 2️⃣ En PythonAnywhere Bash Console
```bash
# Clonar
git clone https://github.com/JuanMero2002/hackaton-prueba.git
cd hackaton-prueba

# Virtual env
mkvirtualenv --python=/usr/bin/python3.10 hackaton-env
pip install -r requirements.txt

# Configurar .env
nano .env
# Pegar tus credenciales de Supabase

# Migraciones y estáticos
python manage.py migrate
python manage.py collectstatic --noinput
```

### 3️⃣ Web App Configuration
- **Source code**: `/home/TUUSUARIO/hackaton-prueba`
- **Working directory**: `/home/TUUSUARIO/hackaton-prueba`
- **Virtualenv**: `/home/TUUSUARIO/.virtualenvs/hackaton-env`

### 4️⃣ WSGI File
Editar y pegar:
```python
import os, sys
path = '/home/TUUSUARIO/hackaton-prueba'
sys.path.insert(0, path)

from dotenv import load_dotenv
load_dotenv(os.path.join(path, '.env'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'sistema_practicas.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 5️⃣ Static Files
- `/static/` → `/home/TUUSUARIO/hackaton-prueba/staticfiles`
- `/media/` → `/home/TUUSUARIO/hackaton-prueba/media`

### ✅ Reload
Botón verde **"Reload"** en la pestaña Web

---

## 📝 .env en PythonAnywhere

```env
SUPABASE_URL=https://owrgthzfdlnhkiwzdgbd.supabase.co
SUPABASE_KEY=tu_anon_key
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=Milxi26.
DB_HOST=db.owrgthzfdlnhkiwzdgbd.supabase.co
DB_PORT=5432
SECRET_KEY=django-insecure-^o$qnv_*2$h_j6+9ci7+i2%d1r+k!#$j_#967*caq9%id-x9*0
DEBUG=False
ALLOWED_HOSTS=tuusuario.pythonanywhere.com,localhost
```

---

## 🔄 Actualizar después de cambios

```bash
cd ~/hackaton-prueba
git pull origin main
workon hackaton-env
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
# Reload en la pestaña Web
```

---

## 🐛 Si hay errores

1. Revisar **Error log** en pestaña Web
2. Verificar `.env` existe: `cat .env`
3. Verificar virtual env activo: `workon hackaton-env`
4. Reinstalar dependencias: `pip install -r requirements.txt`

---

## 📚 Guía completa
Ver: `DEPLOY_PYTHONANYWHERE.md`
