# 🚀 Guía Completa: Instalación de Supabase

## ✅ Paso 1: Crear cuenta en Supabase (GRATIS)

1. Ve a [https://supabase.com](https://supabase.com)
2. Haz clic en **"Start your project"**
3. Regístrate con tu cuenta de GitHub (recomendado) o email
4. Confirma tu email si es necesario

---

## ✅ Paso 2: Crear un nuevo proyecto

1. Una vez dentro, haz clic en **"New Project"**
2. Completa los datos:
   - **Name**: `sistema-practicas-uleam` (o el nombre que prefieras)
   - **Database Password**: Genera una contraseña segura (¡GUÁRDALA BIEN! 🔒)
   - **Region**: Selecciona `South America (São Paulo)` (más cercano a Ecuador)
   - **Pricing Plan**: Selecciona **Free** (0 USD/mes)
3. Haz clic en **"Create new project"**
4. Espera 2-3 minutos mientras se crea el proyecto ⏳

---

## ✅ Paso 3: Obtener las credenciales

### 3.1. Credenciales de la API (para el cliente Supabase)

1. En el menú lateral, ve a **Settings** (⚙️)
2. Haz clic en **API**
3. Copia estos valores:
   - **Project URL**: `https://xxxxxxxxx.supabase.co`
   - **anon/public key**: `eyJhbGciOi...` (clave larga)

### 3.2. Credenciales de PostgreSQL (para Django)

1. En **Settings**, haz clic en **Database**
2. Busca la sección **"Connection string"**
3. Selecciona el modo **"URI"** o **"Pooler"** (recomendado para producción)
4. Copia la cadena de conexión, se verá así:
   ```
   postgresql://postgres.xxxxxxx:[YOUR-PASSWORD]@aws-0-sa-east-1.pooler.supabase.com:6543/postgres
   ```

---

## ✅ Paso 4: Configurar el archivo `.env`

1. Abre el archivo `.env` en la raíz de tu proyecto
2. Completa con tus credenciales:

```env
# ====================================
# CONFIGURACIÓN DE SUPABASE
# ====================================

# URL de tu proyecto Supabase (de Settings > API)
SUPABASE_URL=https://xxxxxxxxx.supabase.co

# Clave anon/public de Supabase (de Settings > API)
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# ====================================
# POSTGRESQL DE SUPABASE
# ====================================

# De Settings > Database > Connection string
DB_NAME=postgres
DB_USER=postgres.xxxxxxxxx
DB_PASSWORD=TU_PASSWORD_DE_SUPABASE
DB_HOST=aws-0-sa-east-1.pooler.supabase.com
DB_PORT=6543

# ====================================
# DJANGO
# ====================================

SECRET_KEY=django-insecure-^o$qnv_*2$h_j6+9ci7+i2%d1r+k!#$j_#967*caq9%id-x9*0
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 📝 Cómo extraer los valores de la cadena de conexión:

Si tu cadena es:
```
postgresql://postgres.abcdef:[PASSWORD]@aws-0-sa-east-1.pooler.supabase.com:6543/postgres
```

Entonces:
- `DB_USER` = `postgres.abcdef`
- `DB_PASSWORD` = Reemplaza `[PASSWORD]` con la contraseña que creaste
- `DB_HOST` = `aws-0-sa-east-1.pooler.supabase.com`
- `DB_PORT` = `6543` (o `5432` si usas conexión directa)
- `DB_NAME` = `postgres`

---

## ✅ Paso 5: Migrar la base de datos

Una vez configurado el `.env`, ejecuta estos comandos:

```powershell
# 1. Crear las tablas en Supabase
python manage.py makemigrations
python manage.py migrate

# 2. Crear un superusuario
python manage.py createsuperuser

# 3. (Opcional) Cargar datos iniciales
python manage.py loaddata inscripciones/fixtures/carreras.json
```

---

## ✅ Paso 6: Verificar la conexión

Abre el **SQL Editor** en Supabase:

1. Ve a **SQL Editor** en el menú lateral
2. Ejecuta esta consulta:

```sql
SELECT 
    schemaname,
    tablename 
FROM pg_tables 
WHERE schemaname = 'public'
ORDER BY tablename;
```

Deberías ver todas las tablas de Django creadas:
- `auth_user`
- `inscripciones_estudiante`
- `inscripciones_empresa`
- `inscripciones_practica`
- `inscripciones_calificacion`
- etc.

---

## 🎯 Ventajas de Supabase

✅ **PostgreSQL completo** (más potente que SQLite)
✅ **Base de datos en la nube** (accesible desde cualquier lugar)
✅ **Panel de administración visual** (Table Editor, SQL Editor)
✅ **Backups automáticos** (plan gratuito: 7 días)
✅ **Autenticación integrada** (puedes usarla en el futuro)
✅ **Storage para archivos** (ideal para CVs y documentos)
✅ **API REST automática** (si la necesitas)
✅ **Límites generosos en el plan gratuito**:
   - 500 MB de base de datos
   - 1 GB de almacenamiento
   - 2 GB de transferencia/mes
   - Proyectos ilimitados

---

## 🔧 Comandos útiles

### Crear migraciones
```powershell
python manage.py makemigrations
```

### Aplicar migraciones
```powershell
python manage.py migrate
```

### Ver estado de migraciones
```powershell
python manage.py showmigrations
```

### Abrir shell de Django conectado a Supabase
```powershell
python manage.py shell
```

### Exportar datos de SQLite (si ya tienes datos)
```powershell
python manage.py dumpdata > datos_backup.json
```

### Importar datos a Supabase
```powershell
python manage.py loaddata datos_backup.json
```

---

## 🚨 Solución de Problemas Comunes

### Error: "connection refused"
- ✅ Verifica que `DB_HOST` y `DB_PORT` sean correctos
- ✅ Asegúrate de que tu firewall permita conexiones SSL

### Error: "password authentication failed"
- ✅ Verifica que `DB_PASSWORD` sea correcto
- ✅ En Supabase, ve a Settings > Database y resetea la contraseña si es necesario

### Error: "SSL connection is required"
- ✅ Ya está configurado en `settings.py` con `'sslmode': 'require'`

### Error: "database does not exist"
- ✅ Usa `DB_NAME=postgres` (nombre por defecto de Supabase)

---

## 📊 Explorar tus datos en Supabase

1. Ve a **Table Editor** en el menú lateral
2. Verás todas tus tablas de Django
3. Puedes:
   - Ver registros
   - Editar datos
   - Agregar filas manualmente
   - Ejecutar consultas SQL
   - Exportar a CSV

---

## 🔐 Seguridad

⚠️ **IMPORTANTE**:
- ✅ NUNCA subas el archivo `.env` a GitHub (ya está en `.gitignore`)
- ✅ Usa contraseñas seguras para Supabase
- ✅ En producción, cambia `DEBUG=False`
- ✅ Configura Row Level Security (RLS) en Supabase si es necesario

---

## 📚 Recursos Adicionales

- [Documentación de Supabase](https://supabase.com/docs)
- [Supabase con Django](https://supabase.com/docs/guides/integrations/django)
- [Dashboard de Supabase](https://supabase.com/dashboard)

---

## ✅ Checklist Final

Antes de continuar, verifica:

- [ ] Proyecto creado en Supabase
- [ ] Archivo `.env` completado con todas las credenciales
- [ ] Dependencias instaladas (`psycopg2-binary`, `supabase`, `python-decouple`)
- [ ] Migraciones ejecutadas exitosamente
- [ ] Superusuario creado
- [ ] Puedes ver las tablas en Supabase Table Editor
- [ ] El servidor Django funciona correctamente

---

¡Todo listo! 🎉 Ahora tu aplicación Django está conectada a Supabase.
