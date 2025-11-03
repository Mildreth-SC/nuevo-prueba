# 🔐 Guía de Acceso al Panel de Administración Django - ULEAM

## 📋 Descripción

El sistema de prácticas ULEAM incluye un **panel de administración completo** basado en Django Admin, personalizado con los colores institucionales de la universidad.

---

## 🎯 Acceso al Panel de Administración

### URL de Acceso
```
http://127.0.0.1:8000/admin/
```

### Credenciales de Superusuario
```
👤 Usuario: admin
🔑 Contraseña: admin123
```

⚠️ **IMPORTANTE**: Cambia esta contraseña en producción.

---

## 🚀 Cómo Iniciar Sesión

### Opción 1: Desde la Página Principal
1. Ve a http://127.0.0.1:8000/
2. Haz clic en "Iniciar Sesión"
3. En el formulario de login, verás un enlace "⚙️ Acceso Administrador"
4. Haz clic en ese enlace
5. Ingresa las credenciales del administrador

### Opción 2: Acceso Directo
1. Ve directamente a http://127.0.0.1:8000/admin/
2. Ingresa usuario: `admin`
3. Ingresa contraseña: `admin123`
4. Haz clic en "Iniciar Sesión"

---

## 🎨 Personalización del Admin

### Estilos Personalizados
El panel de administración ha sido personalizado con:
- ✅ Colores institucionales ULEAM (Rojo #C41E3A y Verde #228B22)
- ✅ Gradientes en header y botones
- ✅ Bordes redondeados modernos
- ✅ Sombras y efectos hover
- ✅ Tipografía mejorada

### Archivos Personalizados
```
templates/admin/
├── base_site.html      # Personalización general del admin
└── login.html          # Página de login personalizada
```

---

## 📊 Funcionalidades del Admin

### 1. **Gestión de Carreras**
- Ver todas las carreras
- Crear, editar y eliminar carreras
- Activar/desactivar carreras
- Búsqueda por nombre y código

### 2. **Gestión de Estudiantes**
- Lista completa de estudiantes
- Filtrado por carrera, ciclo y estado
- Búsqueda por código, nombre y email
- Ver fecha de registro
- Información de usuario asociado

### 3. **Gestión de Empresas**
- Administrar empresas registradas
- Ver RUC, sector y contacto
- Activar/desactivar empresas
- Organización por campos con fieldsets
- Usuario del sistema asociado (colapsable)

**Fieldsets disponibles**:
- Información Básica (nombre, RUC, sector, logo)
- Contacto (responsable, email, teléfono, dirección)
- Detalles (descripción, activa, fecha registro)
- Usuario del Sistema (user)

### 4. **Gestión de Facultades**
- Administrar facultades ULEAM
- Ver código, decano y contacto
- Activar/desactivar facultades
- Organización similar a empresas

### 5. **Gestión de Prácticas**
- Ver todas las prácticas externas
- Filtrar por estado, empresa y fecha
- Búsqueda por título y empresa
- Ver cupos disponibles
- **Acciones masivas**:
  - ✅ Activar prácticas seleccionadas
  - ✅ Desactivar prácticas seleccionadas

### 6. **Gestión de Prácticas Internas**
- Administrar prácticas de facultades
- Filtrar por tipo de servicio
- Ver cupos y fechas
- Jerarquía de fechas

### 7. **Gestión de Inscripciones**
- Ver todas las inscripciones externas
- Filtrar por estado y empresa
- Ver fechas de inscripción y evaluación
- **Acciones masivas**:
  - ✅ Aprobar inscripciones seleccionadas
  - ✅ Rechazar inscripciones seleccionadas

### 8. **Gestión de Inscripciones Internas**
- Administrar inscripciones a prácticas internas
- Filtrar por estado y facultad
- Acciones masivas de aprobación/rechazo

### 9. **Gestión de Documentos**
- Ver documentos subidos por estudiantes
- Filtrar por tipo y fecha
- Búsqueda por nombre

---

## 🔧 Acciones Masivas Disponibles

### En Prácticas
```python
✅ Activar prácticas seleccionadas
❌ Desactivar prácticas seleccionadas
```

### En Inscripciones
```python
✅ Aprobar inscripciones seleccionadas
❌ Rechazar inscripciones seleccionadas
```

### Cómo usar acciones masivas:
1. Selecciona los elementos con los checkboxes
2. Elige la acción en el dropdown "Acción"
3. Haz clic en "Ir"
4. Confirma la acción

---

## 👥 Gestión de Usuarios

### Crear Nuevo Usuario Administrador
Desde el panel de admin:
1. Ve a "Autenticación y autorización" → "Usuarios"
2. Haz clic en "Agregar Usuario"
3. Completa los datos
4. Marca "Es staff" y "Es superusuario" si aplica
5. Guarda

### Desde Línea de Comandos
```bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla.

---

## 🔍 Filtros y Búsquedas

### Carreras
- **Filtros**: Activa/Inactiva
- **Búsqueda**: Nombre, código

### Estudiantes
- **Filtros**: Carrera, Ciclo actual, Activo/Inactivo
- **Búsqueda**: Código, nombre, apellido, email

### Empresas
- **Filtros**: Sector, Activa/Inactiva
- **Búsqueda**: Nombre, RUC, contacto responsable

### Prácticas
- **Filtros**: Estado, Empresa, Fecha de inicio, Activa/Inactiva
- **Búsqueda**: Título, empresa, descripción
- **Jerarquía**: Por fecha de inicio

### Inscripciones
- **Filtros**: Estado, Fecha de inscripción, Empresa
- **Búsqueda**: Nombre estudiante, título práctica
- **Jerarquía**: Por fecha de inscripción

---

## 📱 Interfaz Responsive

El panel de administración es **responsive** y funciona en:
- 💻 Desktop (1920x1080 o superior)
- 💻 Laptop (1366x768 o superior)
- 📱 Tablet (768x1024)
- 📱 Móvil (375x667 o superior)

---

## 🎨 Colores del Sistema

### Colores Institucionales ULEAM
```css
--uleam-red: #C41E3A      /* Rojo principal */
--uleam-green: #228B22    /* Verde institucional */
--uleam-blue: #1E3A8A     /* Azul complementario */
```

### Aplicación
- **Header**: Gradiente rojo → verde
- **Breadcrumbs**: Verde sólido
- **Botones**: Rojo (hover: verde)
- **Enlaces**: Rojo (hover: verde)
- **Tablas**: Header rojo
- **Mensajes de éxito**: Verde
- **Mensajes de error**: Rojo #DC3545

---

## 📊 Estadísticas y Reports

### Desde el Dashboard
El panel principal muestra:
- Total de usuarios registrados
- Modelos disponibles con acceso rápido
- Acciones recientes realizadas

### Reportes Personalizados
Para exportar datos:
1. Ve al modelo deseado
2. Selecciona los registros
3. Usa acciones masivas o exporta manualmente

---

## 🔒 Seguridad

### Niveles de Acceso

#### Superusuario (admin)
- ✅ Acceso total al admin
- ✅ Gestión de todos los modelos
- ✅ Gestión de usuarios
- ✅ Permisos completos

#### Staff (Opcional)
Puedes crear usuarios staff con permisos limitados:
1. Marca "Es staff"
2. NO marques "Es superusuario"
3. Asigna permisos específicos por modelo

#### Usuarios Normales
- ❌ NO tienen acceso al admin
- ✅ Usan el sistema de prácticas normal
- ✅ Paneles específicos (estudiante/empresa/facultad)

### Permisos por Modelo
Cada modelo tiene 4 permisos básicos:
- 👁️ Ver (view)
- ➕ Agregar (add)
- ✏️ Cambiar (change)
- 🗑️ Eliminar (delete)

---

## 🛠️ Mantenimiento

### Limpieza de Sesiones
```bash
python manage.py clearsessions
```

### Backup de Base de Datos
```bash
# SQLite (por defecto)
copy db.sqlite3 db_backup_$(date +%Y%m%d).sqlite3
```

### Ver Logs de Admin
Los cambios realizados en el admin se registran automáticamente en:
- Panel Admin → "Registro" (si está activado)
- Django logs

---

## 🚨 Solución de Problemas

### Error: "CSRF verification failed"
**Solución**: Limpia las cookies del navegador o usa ventana de incógnito.

### Error: "No se puede acceder al admin"
**Verificar**:
1. Usuario tiene `is_staff = True`
2. Usuario tiene `is_superuser = True` (para acceso completo)
3. URL correcta: http://127.0.0.1:8000/admin/

### Error: "Página no encontrada (404)"
**Verificar**:
1. Servidor Django está corriendo
2. URL incluye `/admin/` al final
3. Migraciones aplicadas: `python manage.py migrate`

### Admin sin estilos
**Solución**:
```bash
python manage.py collectstatic
```

---

## 📚 Documentación Adicional

### Django Admin Oficial
https://docs.djangoproject.com/en/5.2/ref/contrib/admin/

### Personalización Avanzada
- `admin.py`: Configuración de modelos en el admin
- `templates/admin/`: Plantillas personalizadas
- `static/admin/`: Archivos estáticos (CSS, JS, imágenes)

---

## 🎯 Mejores Prácticas

### Seguridad
1. ✅ Cambiar contraseña por defecto
2. ✅ Usar HTTPS en producción
3. ✅ Limitar acceso por IP si es posible
4. ✅ Activar autenticación de dos factores (2FA)
5. ✅ Auditar logs regularmente

### Gestión de Datos
1. ✅ Hacer backups regulares
2. ✅ Usar acciones masivas con precaución
3. ✅ Verificar antes de eliminar registros
4. ✅ Mantener datos de contacto actualizados

### Performance
1. ✅ Usar filtros para limitar resultados
2. ✅ Configurar `list_per_page` apropiadamente
3. ✅ Usar `select_related` y `prefetch_related` en queries
4. ✅ Indexar campos frecuentemente buscados

---

## 📞 Soporte

### Contacto
- **Email**: admin@uleam.edu.ec
- **Sistema**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

### Documentación Interna
- `README.md` - Información general
- `GUIA_EMPRESA_FACULTAD.md` - Guía empresas/facultades
- `CONTROL_ACCESO_EMPRESAS_FACULTADES.md` - Seguridad
- `MEJORAS_DISEÑO.md` - Sistema de diseño

---

**Última actualización**: 31 de Octubre de 2025  
**Versión**: 2.0  
**Sistema**: ULEAM - Prácticas Pre Profesionales  
**Estado**: ✅ Operativo

