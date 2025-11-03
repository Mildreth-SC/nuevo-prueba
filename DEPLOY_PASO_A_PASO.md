# 🚀 Guía Completa: Deploy en PythonAnywhere

## 📋 PREPARACIÓN PREVIA (EN TU PC)

### ✅ Checklist Antes de Subir a GitHub

- [x] Base de datos Supabase configurada y funcionando
- [x] Datos de prueba cargados (8 empresas, 12 estudiantes, etc.)
- [x] `.env` con credenciales (NO se sube a GitHub)
- [x] `.gitignore` configurado
- [x] `requirements.txt` actualizado
- [x] Aplicación funcionando localmente

---

## 🌐 PASO 1: SUBIR A GITHUB

### 1.1 Verificar Git
```bash
git status
```

### 1.2 Agregar Cambios
```bash
git add .
git status
```

### 1.3 Commit
```bash
git commit -m "Base de datos Supabase configurada con datos de prueba"
```

### 1.4 Push a GitHub
```bash
git push origin main
```

Si es la primera vez:
```bash
git remote add origin https://github.com/JuanMero2002/hackaton-prueba.git
git branch -M main
git push -u origin main
```

---

## 🐍 PASO 2: CONFIGURAR PYTHONANYWHERE

### 2.1 Crear Cuenta
1. Ve a: https://www.pythonanywhere.com
2. Crea una cuenta **GRATUITA** ("Beginner" plan)
3. Confirma tu email

### 2.2 Abrir Bash Console
1. En el Dashboard, ve a **"Consoles"**
2. Click en **"Bash"**
3. Se abrirá una terminal

---

## 📥 PASO 3: CLONAR PROYECTO

En la consola Bash de PythonAnywhere:

```bash
# Clonar tu repositorio
git clone https://github.com/JuanMero2002/hackaton-prueba.git

# Entrar al directorio
cd hackaton-prueba

# Verificar que todo está ahí
ls -la
```

---

## 🔧 PASO 4: CREAR ENTORNO VIRTUAL

```bash
# Crear virtualenv con Python 3.10
mkvirtualenv --python=/usr/bin/python3.10 hackaton-env

# El prompt cambiará a: (hackaton-env) $

# Instalar dependencias
pip install -r requirements.txt
```

**⏱️ Esto tomará unos minutos. Espera a que termine.**

---

## 🔑 PASO 5: CONFIGURAR VARIABLES DE ENTORNO

```bash
# Crear archivo .env
nano .env
```

Copia y pega EXACTAMENTE esto (usa tus credenciales reales):

```env
# Django
SECRET_KEY=tu-secret-key-aqui
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
SUPABASE_KEY=tu-supabase-anon-key
```

**Importante:**
- Cambia `tuusuario` por tu nombre de usuario de PythonAnywhere
- Usa tu `SECRET_KEY` real de Django
- Usa tu `SUPABASE_KEY` (la encuentras en Supabase Dashboard → Settings → API)

**Para guardar y salir:**
- Presiona `Ctrl + X`
- Presiona `Y` (Yes)
- Presiona `Enter`

---

## 📊 PASO 6: VERIFICAR BASE DE DATOS

```bash
# Activar entorno virtual (si no está activo)
workon hackaton-env

# Verificar conexión a Supabase
python manage.py check

# Ver migraciones
python manage.py showmigrations

# Si todo está bien, NO necesitas hacer migrate porque ya tienes los datos en Supabase
```

---

## 📁 PASO 7: RECOLECTAR ARCHIVOS ESTÁTICOS

```bash
# Crear directorio para archivos estáticos
mkdir -p /home/tuusuario/hackaton-prueba/staticfiles

# Recolectar archivos estáticos
python manage.py collectstatic --noinput
```

---

## 🌍 PASO 8: CONFIGURAR WEB APP

### 8.1 Crear Web App

1. Ve al Dashboard de PythonAnywhere
2. Click en la pestaña **"Web"**
3. Click en **"Add a new web app"**
4. Click **"Next"** (acepta el dominio gratuito)
5. Selecciona **"Manual configuration"**
6. Selecciona **"Python 3.10"**
7. Click **"Next"**

### 8.2 Configurar Virtualenv

En la sección **"Virtualenv"**:
```
/home/tuusuario/.virtualenvs/hackaton-env
```
(Reemplaza `tuusuario` con tu usuario)

### 8.3 Configurar WSGI

1. Click en el link del archivo **WSGI configuration file**
2. **Borra TODO** el contenido
3. Copia y pega esto:

```python
import os
import sys

# Agregar el directorio del proyecto al path
path = '/home/tuusuario/hackaton-prueba'
if path not in sys.path:
    sys.path.append(path)

# Configurar Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'sistema_practicas.settings'

# Cargar variables de entorno desde .env
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('/home/tuusuario/hackaton-prueba/.env')
load_dotenv(dotenv_path=env_path)

# Inicializar Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Importante:** Reemplaza `tuusuario` con tu nombre de usuario en TODAS las líneas.

4. Click **"Save"** (arriba a la derecha)

### 8.4 Configurar Archivos Estáticos

Vuelve a la pestaña **"Web"** y en la sección **"Static files"**:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/tuusuario/hackaton-prueba/staticfiles/` |
| `/media/` | `/home/tuusuario/hackaton-prueba/media/` |

(Reemplaza `tuusuario` con tu usuario)

---

## 🎯 PASO 9: ACTUALIZAR SETTINGS.PY

Vuelve a la consola Bash:

```bash
cd ~/hackaton-prueba
nano sistema_practicas/settings.py
```

Busca la línea `ALLOWED_HOSTS` y actualízala:

```python
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')
```

**Para guardar:** `Ctrl + X`, luego `Y`, luego `Enter`

---

## ✅ PASO 10: RECARGAR Y PROBAR

### 10.1 Recargar la Web App

1. Ve a la pestaña **"Web"** en PythonAnywhere
2. Click en el botón verde **"Reload tuusuario.pythonanywhere.com"**
3. Espera unos segundos

### 10.2 Probar la Aplicación

Abre en tu navegador:
```
https://tuusuario.pythonanywhere.com
```

**Deberías ver tu aplicación funcionando!** 🎉

### 10.3 Probar Login

Prueba con las credenciales de prueba:

**Como Estudiante:**
- Usuario: `est1312345678`
- Contraseña: `estudiante123`

**Como Empresa:**
- Usuario: `techsolutions_ecuador`
- Contraseña: `empresa123`

**Como Admin:**
- Usuario: `Mildreth`
- URL: `https://tuusuario.pythonanywhere.com/admin`

---

## 🔍 PASO 11: VERIFICAR LOGS (Si hay errores)

Si algo no funciona:

```bash
# Ver log de errores
tail -f /var/log/tuusuario.pythonanywhere.com.error.log

# Ver log de acceso
tail -f /var/log/tuusuario.pythonanywhere.com.access.log
```

Presiona `Ctrl + C` para salir.

---

## 🐛 SOLUCIÓN DE PROBLEMAS COMUNES

### Error: "DisallowedHost"
**Solución:** Verifica que `ALLOWED_HOSTS` en `.env` incluya tu dominio de PythonAnywhere.

### Error: "OperationalError: could not connect to server"
**Solución:** Verifica las credenciales de Supabase en `.env` y que `DB_HOST` tenga el puerto correcto.

### Error: "Static files not loading"
**Solución:**
```bash
cd ~/hackaton-prueba
workon hackaton-env
python manage.py collectstatic --noinput
```
Luego recarga la web app.

### Error: "ImportError: No module named..."
**Solución:**
```bash
workon hackaton-env
pip install -r requirements.txt
```
Luego recarga la web app.

---

## 🔄 ACTUALIZAR LA APLICACIÓN

Cuando hagas cambios en tu código local:

### En tu PC:
```bash
git add .
git commit -m "Descripción de los cambios"
git push origin main
```

### En PythonAnywhere Bash:
```bash
cd ~/hackaton-prueba
git pull origin main

workon hackaton-env
pip install -r requirements.txt  # Solo si actualizaste dependencias

python manage.py collectstatic --noinput  # Solo si cambiaste CSS/JS
```

### Recargar:
- Ve a Web → Click en "Reload"

---

## 📊 MONITOREO

### Ver usuarios en Supabase
1. https://supabase.com/dashboard
2. Selecciona tu proyecto
3. Table Editor → Ver todas las tablas

### Ver logs en tiempo real
```bash
tail -f /var/log/tuusuario.pythonanywhere.com.error.log
```

---

## ⚡ COMANDOS ÚTILES

```bash
# Activar entorno virtual
workon hackaton-env

# Ver entornos virtuales disponibles
lsvirtualenv

# Actualizar código desde GitHub
cd ~/hackaton-prueba && git pull

# Ver procesos de Python
ps aux | grep python

# Limpiar cache de Python
find . -type d -name __pycache__ -exec rm -r {} +

# Ver espacio en disco
df -h
```

---

## 📝 NOTAS IMPORTANTES

1. **Plan Gratuito de PythonAnywhere:**
   - 1 web app
   - 512 MB de espacio
   - Dominio: `tuusuario.pythonanywhere.com`
   - Solo HTTPS habilitados (no puedes usar APIs externas)

2. **Supabase Free Tier:**
   - 500 MB de base de datos
   - 50,000 peticiones/mes
   - Perfecto para demos y desarrollo

3. **La aplicación se "duerme" después de 3 meses sin actividad en el plan gratuito**

4. **Backups:** Los datos están en Supabase, que hace backups automáticos

---

## ✅ CHECKLIST FINAL

- [ ] Código subido a GitHub
- [ ] Cuenta PythonAnywhere creada
- [ ] Proyecto clonado en PythonAnywhere
- [ ] Virtualenv creado e instaladas dependencias
- [ ] Archivo `.env` configurado
- [ ] Web App creada y configurada
- [ ] WSGI configurado correctamente
- [ ] Static files configurados
- [ ] Aplicación recargada
- [ ] Aplicación funcionando en navegador
- [ ] Login probado con diferentes usuarios
- [ ] Admin panel accesible

---

## 🎉 ¡LISTO!

Tu aplicación ahora está **ONLINE** y accesible desde cualquier lugar del mundo en:

```
https://tuusuario.pythonanywhere.com
```

**Comparte el link con:**
- Tus profesores
- Compañeros de equipo
- Evaluadores del hackathon
- Potenciales usuarios

---

## 📞 SOPORTE

Si tienes problemas:
1. Revisa los logs en PythonAnywhere
2. Verifica la conexión a Supabase
3. Consulta la documentación: https://help.pythonanywhere.com
4. Revisa los errores en la consola Bash

---

**¡Éxito con tu hackathon! 🚀**
