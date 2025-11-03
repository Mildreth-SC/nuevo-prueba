# 🚀 Guía de Despliegue en Vercel

Esta guía te ayudará a desplegar tu aplicación Django en Vercel de forma gratuita.

## 📋 Archivos de Configuración Creados

- `vercel.json` - Configuración principal de Vercel
- `vercel_build.sh` - Script de construcción
- `wsgi_vercel.py` - Handler WSGI para Vercel

## 🔧 Preparación

### 1. Asegúrate de que tu código esté en GitHub

```bash
git add .
git commit -m "Preparar para despliegue en Vercel"
git push origin main
```

## 🌐 Despliegue en Vercel

### Paso 1: Crear Cuenta en Vercel

1. Ve a [vercel.com](https://vercel.com)
2. Haz clic en **"Sign Up"**
3. Selecciona **"Continue with GitHub"**
4. Autoriza a Vercel para acceder a tu cuenta de GitHub

### Paso 2: Importar tu Proyecto

1. En el dashboard de Vercel, haz clic en **"Add New Project"**
2. Selecciona **"Import Git Repository"**
3. Busca tu repositorio **"nuevo-prueba"** y haz clic en **"Import"**

### Paso 3: Configurar el Proyecto

En la página de configuración:

1. **Framework Preset:** Selecciona **"Other"**
2. **Root Directory:** Deja el valor por defecto (`.`)
3. **Build Command:** `bash vercel_build.sh`
4. **Output Directory:** `staticfiles`

### Paso 4: Configurar Variables de Entorno

Haz clic en **"Environment Variables"** y agrega las siguientes variables:

| Variable | Valor | Descripción |
|----------|-------|-------------|
| `SECRET_KEY` | Tu SECRET_KEY de Django | Clave secreta de Django |
| `DEBUG` | `False` | Modo debug (siempre False en producción) |
| `ALLOWED_HOSTS` | `.vercel.app,localhost` | Hosts permitidos |
| `DB_NAME` | `postgres` | Nombre de la base de datos |
| `DB_USER` | `postgres.owrgthzfdlnhkiwzdgbd` | Usuario de PostgreSQL |
| `DB_PASSWORD` | `Milxi26.` | Contraseña de PostgreSQL |
| `DB_HOST` | `aws-0-us-east-1.pooler.supabase.com` | Host de Supabase Pooler |
| `DB_PORT` | `6543` | Puerto de Supabase Pooler |
| `SUPABASE_URL` | Tu URL de Supabase | URL del proyecto Supabase |
| `SUPABASE_KEY` | Tu API Key de Supabase | Clave API de Supabase |

> **⚠️ IMPORTANTE:** Usa el **Connection Pooler de Supabase** para evitar problemas de conexión:
> - Host: `aws-0-us-east-1.pooler.supabase.com`
> - Port: `6543`
> - User: `postgres.owrgthzfdlnhkiwzdgbd` (formato: postgres.PROYECTO_ID)

### Paso 5: Desplegar

1. Haz clic en **"Deploy"**
2. Vercel comenzará a construir y desplegar tu aplicación
3. Espera a que termine el proceso (puede tardar 2-5 minutos)

## ✅ Verificación

Una vez completado el despliegue:

1. Vercel te dará una URL del tipo: `https://tu-proyecto.vercel.app`
2. Visita esa URL para verificar que tu aplicación funciona
3. Prueba el login y las funcionalidades principales

## 🔍 Solución de Problemas

### Error: "Network is unreachable"

**Causa:** Problemas de conectividad IPv6 con Supabase.

**Solución:** Asegúrate de usar el Connection Pooler de Supabase:
- DB_HOST: `aws-0-us-east-1.pooler.supabase.com`
- DB_PORT: `6543`
- DB_USER: `postgres.owrgthzfdlnhkiwzdgbd`

### Error: "Application Error"

**Causa:** Variables de entorno no configuradas correctamente.

**Solución:**
1. Ve a tu proyecto en Vercel
2. Click en **"Settings"** → **"Environment Variables"**
3. Verifica que todas las variables estén configuradas
4. Haz clic en **"Redeploy"** en la pestaña **"Deployments"**

### Error: "Static files not found"

**Causa:** Archivos estáticos no recolectados correctamente.

**Solución:**
1. Verifica que `vercel_build.sh` tenga permisos de ejecución
2. Asegúrate de que `STATIC_ROOT` esté configurado en `settings.py`
3. Redespliega el proyecto

### Error de Base de Datos durante migraciones

**Causa:** Base de datos no accesible durante el build.

**Solución:**
1. Verifica las credenciales de Supabase
2. Confirma que el Connection Pooler esté funcionando
3. Considera comentar `python manage.py migrate` en `vercel_build.sh` si las migraciones ya están aplicadas

## 🔄 Actualizar el Despliegue

Cada vez que hagas `git push` a tu rama `main`, Vercel automáticamente:
1. Detectará los cambios
2. Construirá una nueva versión
3. Desplegará la actualización

## 📊 Limitaciones de Vercel (Plan Gratuito)

- **Duración de función:** Máximo 10 segundos por request
- **Tamaño de función:** Máximo 50MB
- **Bandwidth:** 100GB/mes
- **Invocaciones:** Ilimitadas (con fair use)

## 🎯 Consideraciones Importantes

1. **Archivos Estáticos:** Vercel maneja archivos estáticos automáticamente con WhiteNoise
2. **Base de Datos:** Debes usar una base de datos externa (Supabase)
3. **Media Files:** Vercel no es ideal para archivos media subidos por usuarios. Considera usar S3 o Cloudinary
4. **Serverless:** Django se ejecuta en modo serverless, cada request inicia la aplicación

## 🆘 Soporte

Si tienes problemas:
1. Revisa los logs en Vercel: **Deployments** → Click en el deployment → **View Function Logs**
2. Verifica las variables de entorno
3. Consulta la [documentación de Vercel](https://vercel.com/docs)

## 🎉 ¡Listo!

Tu aplicación Django ahora está desplegada en Vercel. Comparte tu URL `.vercel.app` con quien necesites.

---

**Creado:** Noviembre 2025  
**Proyecto:** Sistema de Prácticas Profesionales
