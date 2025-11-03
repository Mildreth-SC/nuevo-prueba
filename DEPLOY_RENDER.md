# 🚀 Deploy en Render.com - Guía Completa

## ✅ INFORMACIÓN
- **Repositorio:** https://github.com/Mildreth-SC/nuevo-prueba
- **Plataforma:** Render.com (100% GRATIS)
- **Base de datos:** Supabase PostgreSQL

---

## 📋 REQUISITOS

✅ Cuenta de GitHub (ya la tienes)
✅ Repositorio pusheado (ya lo tienes)
✅ Base de datos Supabase (ya la tienes)

---

## PASO 1: SUBIR CAMBIOS A GITHUB

Primero, sube los nuevos archivos a GitHub:

```powershell
git add .
git commit -m "Add Render.com deployment files"
git push origin main
```

---

## PASO 2: CREAR CUENTA EN RENDER

1. Ve a: **https://render.com**
2. Click en **"Get Started for Free"**
3. Click en **"Sign in with GitHub"**
4. Autoriza a Render para acceder a tus repositorios

---

## PASO 3: CREAR WEB SERVICE

1. En el Dashboard de Render, click en **"New +"** (arriba a la derecha)
2. Selecciona **"Web Service"**

---

## PASO 4: CONECTAR REPOSITORIO

1. Busca **"nuevo-prueba"** en la lista
2. Click en **"Connect"**

---

## PASO 5: CONFIGURAR EL SERVICIO

Llena el formulario con estos datos:

### **Name:**
```
sistema-practicas
```

### **Region:**
```
Oregon (US West) o la más cercana
```

### **Branch:**
```
main
```

### **Runtime:**
```
Python 3
```

### **Build Command:**
```
chmod +x build.sh && ./build.sh
```

### **Start Command:**
```
gunicorn sistema_practicas.wsgi:application
```

### **Instance Type:**
```
Free
```

---

## PASO 6: CONFIGURAR VARIABLES DE ENTORNO

Scroll hasta la sección **"Environment Variables"** y agrega estas (una por una):

Click en **"Add Environment Variable"** y agrega:

### 1. SECRET_KEY
```
django-insecure-7cj+9fy6a^n3_i8z2k&x*y7(v)#gf+s@4r$q^2h-7&d*+1
```

### 2. DEBUG
```
False
```

### 3. DB_NAME
```
postgres
```

### 4. DB_USER
```
postgres
```

### 5. DB_PASSWORD
```
Milxi26.
```

### 6. DB_HOST
```
db.owrgthzfdlnhkiwzdgbd.supabase.co
```

### 7. DB_PORT
```
5432
```

### 8. SUPABASE_URL
```
https://owrgthzfdlnhkiwzdgbd.supabase.co
```

### 9. SUPABASE_KEY
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im93cmd0aHpmZGxuaGtpd3pkZ2JkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzA0Njk4MTYsImV4cCI6MjA0NjA0NTgxNn0.K7X3qCjYZ8QnN5fGX6kGTXV7yHVqZXhI5pQrLmNjK4Y
```

### 10. PYTHON_VERSION
```
3.10.0
```

---

## PASO 7: AGREGAR ALLOWED_HOSTS AUTOMÁTICO

Scroll hasta **"Advanced"** y agrega una variable más:

### RENDER_EXTERNAL_HOSTNAME
```
(déjala vacía, Render la llenará automáticamente)
```

---

## PASO 8: CREAR EL SERVICIO

1. Click en **"Create Web Service"** (abajo)
2. ⏱️ Espera 3-5 minutos mientras Render:
   - Clona tu repositorio
   - Instala las dependencias
   - Ejecuta las migraciones
   - Colecta archivos estáticos
   - Inicia la aplicación

---

## PASO 9: ACTUALIZAR ALLOWED_HOSTS

Una vez que el deploy termine:

1. Copia la URL que Render te dio (algo como: `sistema-practicas-xxxx.onrender.com`)
2. Ve a tu computadora y abre `sistema_practicas/settings.py`
3. Busca la línea `ALLOWED_HOSTS` y agrégala:

```python
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')
```

4. Ve a Render → Tu servicio → **Environment**
5. Edita la variable `DEBUG` si existe o agrega una nueva:

**ALLOWED_HOSTS**
```
.onrender.com
```

6. Click en **"Save Changes"**
7. Render redesplegará automáticamente

---

## PASO 10: ¡PROBAR TU APLICACIÓN!

1. Click en la URL de tu servicio (arriba a la izquierda)
2. ¡Tu aplicación debería estar funcionando! 🎉

**URL:** `https://sistema-practicas-xxxx.onrender.com`

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
- Contraseña: (tu contraseña de superuser)

---

## 🔄 ACTUALIZACIONES FUTURAS

Cada vez que hagas cambios:

```powershell
git add .
git commit -m "Descripción de cambios"
git push origin main
```

¡Render detectará los cambios y redesplegará automáticamente! 🚀

---

## 📊 MONITOREO

En el Dashboard de Render puedes ver:
- **Logs:** Click en "Logs" para ver errores
- **Metrics:** Uso de CPU y RAM
- **Events:** Historial de deploys

---

## ⚠️ IMPORTANTE: TIEMPO DE INACTIVIDAD

Con el plan gratuito:
- Tu app se "duerme" después de 15 minutos sin uso
- La primera petición después de dormir tarda ~30 segundos
- **Solución:** Usar un servicio como [UptimeRobot](https://uptimerobot.com/) para hacer ping cada 14 minutos

---

## 🆘 SI HAY ERRORES

1. Ve a **Logs** en Render
2. Busca el error en rojo
3. Si es de base de datos, verifica las credenciales
4. Si es de archivos estáticos, verifica que `collectstatic` se ejecutó

---

## ✅ RESUMEN

1. ✅ Subir cambios a GitHub
2. ✅ Crear cuenta en Render con GitHub
3. ✅ Conectar repositorio nuevo-prueba
4. ✅ Configurar Build & Start commands
5. ✅ Agregar 10 variables de entorno
6. ✅ Crear Web Service
7. ✅ Esperar 3-5 minutos
8. ✅ Actualizar ALLOWED_HOSTS
9. ✅ ¡Aplicación online!

**Tiempo total: 15 minutos** ⏱️

---

## 🎯 VENTAJAS DE RENDER

✅ **100% Gratis** para siempre
✅ **Deploy automático** desde GitHub
✅ **SSL/HTTPS gratis** incluido
✅ **Soporta Supabase** perfectamente
✅ **Logs en tiempo real**
✅ **Muy fácil de usar**

---

## 🔗 ENLACES ÚTILES

- **Dashboard:** https://dashboard.render.com
- **Documentación:** https://render.com/docs
- **Soporte:** https://render.com/docs/support

---

¡Tu aplicación estará en producción en menos de 15 minutos! 🚀🎉
