# ✅ Pre-Deploy Checklist

## 🎯 ANTES DE SUBIR A GITHUB

### Archivos Esenciales
- [x] `requirements.txt` - Dependencias actualizadas
- [x] `.gitignore` - Archivo configurado (no sube .env, venv, db.sqlite3)
- [x] `.env` - Credenciales Supabase (NO se sube a GitHub)
- [x] `README.md` - Documentación del proyecto
- [x] Guías de deploy creadas

### Base de Datos
- [x] Supabase configurado y funcionando
- [x] Migraciones aplicadas (20 tablas creadas)
- [x] Datos de prueba cargados:
  - 8 Empresas
  - 12 Estudiantes  
  - 9 Prácticas Externas
  - 3 Facultades
  - 3 Prácticas Internas
  - 8 Inscripciones

### Configuración Django
- [x] `settings.py` usando `python-decouple` para variables de entorno
- [x] `DEBUG=True` en local (cambiar a False en producción)
- [x] `ALLOWED_HOSTS` configurado
- [x] Base de datos PostgreSQL (Supabase)
- [x] Static files configurados

### Pruebas Locales
- [x] Servidor corre sin errores: `python manage.py runserver`
- [x] Admin accesible: http://127.0.0.1:8000/admin
- [x] Login funciona para estudiantes, empresas, facultades
- [x] Chatbot responde correctamente
- [x] Inscripciones funcionan

---

## 📤 COMANDOS PARA SUBIR A GITHUB

```powershell
# 1. Ver estado actual
git status

# 2. Agregar todos los cambios
git add .

# 3. Verificar qué se va a subir
git status

# 4. Hacer commit
git commit -m "Deploy ready: Supabase configurado con datos de prueba"

# 5. Subir a GitHub
git push origin main
```

Si es tu primer push:
```powershell
git remote add origin https://github.com/JuanMero2002/hackaton-prueba.git
git branch -M main
git push -u origin main
```

---

## 🔐 INFORMACIÓN SENSIBLE A NO SUBIR

Estos archivos YA están en `.gitignore`:
- ✅ `.env` - Credenciales de Supabase
- ✅ `db.sqlite3` - Base de datos local
- ✅ `venv/` - Entorno virtual
- ✅ `__pycache__/` - Cache de Python
- ✅ `*.pyc` - Archivos compilados

---

## 📋 INFORMACIÓN PARA PYTHONANYWHERE

Necesitarás esta información al configurar PythonAnywhere:

### Credenciales Supabase
```
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=Milxi26.
DB_HOST=db.owrgthzfdlnhkiwzdgbd.supabase.co
DB_PORT=5432
```

### Supabase URLs
```
SUPABASE_URL=https://owrgthzfdlnhkiwzdgbd.supabase.co
```

### Django Secret Key
Genera una nueva para producción:
```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 🚀 PRÓXIMOS PASOS

1. **Subir a GitHub** (comandos arriba)
2. **Crear cuenta en PythonAnywhere**: https://www.pythonanywhere.com
3. **Seguir guía**: `DEPLOY_PASO_A_PASO.md` (tiene todos los pasos detallados)
4. **Tiempo estimado**: 15-20 minutos

---

## 📊 CREDENCIALES DE PRUEBA

Para probar la aplicación después del deploy:

### Estudiante
- Usuario: `est1312345678`
- Contraseña: `estudiante123`

### Empresa
- Usuario: `techsolutions_ecuador`
- Contraseña: `empresa123`

### Facultad
- Usuario: `fci`
- Contraseña: `facultad123`

### Admin (Superusuario)
- Usuario: `Mildreth`
- Email: mildrethguanoluisa@gmail.com
- URL: `/admin`

---

## ✅ VERIFICACIÓN FINAL

Antes de deployar, verifica en local:

```powershell
# 1. Activar entorno virtual
.\venv\Scripts\activate

# 2. Verificar conexión a Supabase
python test_supabase_connection.py

# 3. Verificar que el servidor corre
python manage.py runserver

# 4. Probar en navegador
# http://127.0.0.1:8000
```

Todo debe funcionar SIN errores.

---

## 📁 ARCHIVOS DE DOCUMENTACIÓN CREADOS

- ✅ `DEPLOY_PASO_A_PASO.md` - Guía completa y detallada (LA MÁS IMPORTANTE)
- ✅ `DEPLOY_PYTHONANYWHERE.md` - Guía técnica
- ✅ `DEPLOY_QUICKSTART.md` - Resumen rápido
- ✅ `DATOS_PRUEBA.md` - Información de datos cargados
- ✅ `GUIA_SUPABASE.md` - Configuración Supabase
- ✅ Este checklist

---

## 🎯 ESTÁS LISTO PARA:

- ✅ Subir código a GitHub
- ✅ Deployar en PythonAnywhere
- ✅ Demostrar tu aplicación funcionando
- ✅ Compartir link público
- ✅ Presentar en el hackathon

---

**¡Todo está preparado! 🚀**

**Siguiente paso:** Ejecuta los comandos de Git para subir a GitHub, luego sigue `DEPLOY_PASO_A_PASO.md`
