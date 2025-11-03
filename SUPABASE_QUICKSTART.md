# 🚀 RESUMEN RÁPIDO: Configurar Supabase

## 📝 Checklist de Instalación

### ✅ Paso 1: Cuenta de Supabase
- [ ] Crear cuenta en https://supabase.com
- [ ] Crear nuevo proyecto
- [ ] Guardar contraseña de la base de datos

### ✅ Paso 2: Obtener Credenciales
- [ ] Ir a Settings > API
- [ ] Copiar Project URL
- [ ] Copiar anon/public key
- [ ] Ir a Settings > Database
- [ ] Copiar Connection string (URI o Pooler)

### ✅ Paso 3: Configurar .env
- [ ] Editar archivo `.env` en la raíz del proyecto
- [ ] Pegar `SUPABASE_URL`
- [ ] Pegar `SUPABASE_KEY`
- [ ] Configurar `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`

### ✅ Paso 4: Migrar Base de Datos
```powershell
# Opción A: Base de datos nueva (sin datos previos)
python manage.py migrate
python manage.py createsuperuser

# Opción B: Migrar desde SQLite (si ya tienes datos)
python migrate_to_supabase.py
```

### ✅ Paso 5: Verificar
```powershell
# Probar conexión
python test_supabase_connection.py

# Iniciar servidor
python manage.py runserver
```

---

## 🎯 Ejemplo de .env Configurado

```env
# SUPABASE (Settings > API)
SUPABASE_URL=https://abcdefgh.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdX...

# POSTGRESQL (Settings > Database > Connection String)
DB_NAME=postgres
DB_USER=postgres.abcdefgh
DB_PASSWORD=tu_contraseña_super_segura_123
DB_HOST=aws-0-sa-east-1.pooler.supabase.com
DB_PORT=6543

# DJANGO
SECRET_KEY=django-insecure-^o$qnv_*2$h_j6+9ci7+i2%d1r+k!#$j_#967*caq9%id-x9*0
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## 🔧 Comandos Útiles

```powershell
# Ver estado de migraciones
python manage.py showmigrations

# Crear backup de datos
python manage.py dumpdata > backup.json

# Restaurar datos
python manage.py loaddata backup.json

# Acceder a shell de Django
python manage.py shell

# Crear superusuario
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

---

## 🚨 Problemas Comunes

### "connection refused"
✅ Verifica DB_HOST y DB_PORT

### "password authentication failed"
✅ Verifica DB_PASSWORD

### "SSL connection required"
✅ Ya configurado en settings.py

### No se ven las tablas
✅ Ejecuta: `python manage.py migrate`

---

## 📚 Archivos Importantes

| Archivo | Descripción |
|---------|-------------|
| `.env` | Credenciales (NO SUBIR A GIT) |
| `settings.py` | Configuración de Django |
| `requirements.txt` | Dependencias del proyecto |
| `GUIA_SUPABASE.md` | Guía completa y detallada |
| `test_supabase_connection.py` | Script de prueba |
| `migrate_to_supabase.py` | Script de migración |

---

## ✅ TODO LISTO!

Una vez configurado:
1. Ve a https://supabase.com/dashboard
2. Selecciona tu proyecto
3. Ve a "Table Editor"
4. Deberías ver todas las tablas de Django

¡Ahora tu aplicación usa Supabase! 🎉
