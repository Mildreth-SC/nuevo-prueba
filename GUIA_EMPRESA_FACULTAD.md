# 🏢 GUÍA DE ACCESO: EMPRESAS Y FACULTADES

## 📋 Resumen de Cambios

Se ha implementado completamente el sistema de gestión para **Empresas** y **Facultades**, permitiendo que:

- ✅ Las empresas puedan **publicar prácticas externas** y **gestionar postulantes**
- ✅ Las facultades puedan **publicar prácticas internas** y **evaluar estudiantes**
- ✅ Cada entidad tiene su propio **panel de control** personalizado
- ✅ Sistema completo de **evaluación y aprobación** de postulantes

---

## 🔐 CREDENCIALES DE ACCESO

### 🏢 EMPRESAS (8 empresas disponibles)

| Empresa | Username | Password |
|---------|----------|----------|
| Tech Solutions Ecuador | `empresa_1790123456001` | `empresa123` |
| Constructora del Pacifico | `empresa_1790234567001` | `empresa123` |
| Banco Nacional del Ecuador | `empresa_1790345678001` | `empresa123` |
| Hospital Metropolitano | `empresa_1790456789001` | `empresa123` |
| Estudio Jurídico Asociados | `empresa_1790567890001` | `empresa123` |
| Marketing Digital Pro | `empresa_1790678901001` | `empresa123` |
| Grupo Empresarial Costa | `empresa_1790789012001` | `empresa123` |
| Consultoría y Auditoría CPA | `empresa_1790890123001` | `empresa123` |

### 🎓 FACULTADES (5 facultades disponibles)

| Facultad | Username | Password |
|----------|----------|----------|
| Facultad de Ciencias Administrativas | `facultad_fca` | `facultad123` |
| Facultad de Ciencias Informáticas | `facultad_fci` | `facultad123` |
| Facultad de Ciencias Médicas | `facultad_fcm` | `facultad123` |
| Facultad de Ingeniería | `facultad_fing` | `facultad123` |
| Facultad de Ciencias Sociales | `facultad_fcsd` | `facultad123` |

---

## 🎯 FUNCIONALIDADES IMPLEMENTADAS

### 🏢 PANEL DE EMPRESA

#### 1. **Panel de Control** (`/empresa/panel/`)
- 📊 Dashboard con estadísticas:
  - Total de prácticas publicadas
  - Prácticas activas
  - Total de postulaciones
  - Postulaciones pendientes de evaluación
- 📋 Vista de últimas 5 prácticas publicadas
- 🔗 Accesos rápidos a crear y gestionar prácticas

#### 2. **Gestión de Prácticas** (`/empresa/practicas/`)
- 📝 Crear nueva práctica externa (`/empresa/practicas/crear/`)
- ✏️ Editar prácticas existentes (`/empresa/practicas/<id>/editar/`)
- 🔍 Filtrar prácticas por estado (disponible, en proceso, completada, cancelada)
- 📄 Paginación de resultados

#### 3. **Gestión de Postulantes** (`/empresa/practicas/<id>/postulantes/`)
- 👥 Ver lista completa de postulantes por práctica
- 🔍 Filtrar por estado (pendiente, aprobada, rechazada, cancelada)
- ✅ Evaluar postulantes individualmente (`/empresa/inscripcion/<id>/evaluar/`)
  - Aprobar o rechazar
  - Agregar observaciones
- 📊 Ver información completa del estudiante:
  - Nombre, código, carrera
  - Email, teléfono
  - Fecha de inscripción

#### 4. **Navegación Personalizada**
Al iniciar sesión como empresa, el menú muestra:
- 🏠 Inicio
- 📋 Prácticas
- 🏢 Empresas
- 🎛️ **Panel de Control** (nuevo)
- 💼 **Mis Prácticas** (nuevo)
- ➕ **Nueva Práctica** (nuevo)
- 🚪 Cerrar Sesión

---

### 🎓 PANEL DE FACULTAD

#### 1. **Panel de Control** (`/facultad/panel/`)
- 📊 Dashboard con estadísticas:
  - Total de prácticas internas publicadas
  - Prácticas internas activas
  - Total de postulaciones internas
  - Postulaciones pendientes de evaluación
- 📋 Vista de últimas 5 prácticas internas publicadas
- 🔗 Accesos rápidos a crear y gestionar prácticas

#### 2. **Gestión de Prácticas Internas** (`/facultad/practicas/`)
- 📝 Crear nueva práctica interna (`/facultad/practicas/crear/`)
- ✏️ Editar prácticas internas existentes (`/facultad/practicas/<id>/editar/`)
- 🔍 Filtrar prácticas por estado
- 📄 Paginación de resultados
- 🏷️ Ver tipo de servicio (investigación, docencia, vinculación, administrativa, etc.)

#### 3. **Gestión de Postulantes Internos** (`/facultad/practicas/<id>/postulantes/`)
- 👥 Ver lista completa de postulantes por práctica interna
- 🔍 Filtrar por estado
- ✅ Evaluar postulantes individualmente (`/facultad/inscripcion/<id>/evaluar/`)
  - Aprobar o rechazar
  - Agregar observaciones
- 📊 Ver información completa del estudiante

#### 4. **Navegación Personalizada**
Al iniciar sesión como facultad, el menú muestra:
- 🏠 Inicio
- 📋 Prácticas
- 🏢 Empresas
- 🎛️ **Panel de Control** (nuevo)
- 📚 **Prácticas Internas** (nuevo)
- ➕ **Nueva Práctica** (nuevo)
- 🚪 Cerrar Sesión

---

## 🚀 CÓMO PROBAR EL SISTEMA

### Escenario 1: Empresa publica una práctica

1. **Iniciar sesión como empresa:**
   ```
   Username: empresa_1790123456001
   Password: empresa123
   ```

2. **Ir al Panel de Control:**
   - Clic en "Panel de Control" en el menú superior
   - Verás las estadísticas de tu empresa

3. **Crear una nueva práctica:**
   - Clic en "Nueva Práctica" (botón verde)
   - Completar el formulario:
     - Título: "Desarrollador Web Junior"
     - Descripción, requisitos, duración, etc.
     - Cupos disponibles: 3
     - Fechas de inicio, fin y límite de inscripción
   - Guardar

4. **Ver la práctica publicada:**
   - Clic en "Mis Prácticas"
   - Tu nueva práctica aparecerá en la lista

### Escenario 2: Empresa evalúa postulantes

1. **Ver postulantes:**
   - Desde "Mis Prácticas", clic en "👥 Ver Postulantes"
   - Verás todos los estudiantes que se postularon

2. **Evaluar un postulante:**
   - Clic en "📋 Evaluar"
   - Ver información completa del estudiante
   - Decidir: Aprobar ✅ o Rechazar ❌
   - Agregar observaciones (opcional)
   - Guardar decisión

3. **Ver resultado:**
   - El estado del postulante cambia a "Aprobada" o "Rechazada"
   - Los cupos se actualizan automáticamente

### Escenario 3: Facultad gestiona prácticas internas

1. **Iniciar sesión como facultad:**
   ```
   Username: facultad_fci
   Password: facultad123
   ```

2. **Crear práctica interna:**
   - Clic en "Nueva Práctica"
   - Completar formulario con tipo de servicio (investigación, docencia, etc.)
   - Guardar

3. **Gestionar postulantes:**
   - Similar al proceso de empresa
   - Evaluar, aprobar o rechazar estudiantes

---

## 🔧 CAMBIOS TÉCNICOS REALIZADOS

### 1. **Modelos actualizados** (`inscripciones/models.py`)
```python
class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # ... resto de campos

class Facultad(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # ... resto de campos
```

### 2. **Decoradores completados** (`inscripciones/decorators.py`)
- ✅ `@empresa_required` - Verifica que el usuario sea una empresa
- ✅ `@facultad_required` - Verifica que el usuario sea una facultad
- ✅ `@estudiante_required` - Ya existía

### 3. **Nuevas vistas** (`inscripciones/views.py`)
**Para Empresas:**
- `panel_empresa()` - Dashboard
- `mis_practicas_empresa()` - Lista de prácticas
- `crear_practica_empresa()` - Crear práctica
- `editar_practica_empresa()` - Editar práctica
- `postulantes_practica()` - Ver postulantes
- `evaluar_postulante()` - Aprobar/rechazar

**Para Facultades:**
- `panel_facultad()` - Dashboard
- `mis_practicas_facultad()` - Lista de prácticas internas
- `crear_practica_facultad()` - Crear práctica interna
- `editar_practica_facultad()` - Editar práctica interna
- `postulantes_practica_interna()` - Ver postulantes
- `evaluar_postulante_interno()` - Aprobar/rechazar

### 4. **Nuevas URLs** (`inscripciones/urls.py`)
```python
# Empresa
path('empresa/panel/', ...)
path('empresa/practicas/', ...)
path('empresa/practicas/crear/', ...)
path('empresa/practicas/<int:pk>/editar/', ...)
path('empresa/practicas/<int:pk>/postulantes/', ...)
path('empresa/inscripcion/<int:inscripcion_pk>/evaluar/', ...)

# Facultad
path('facultad/panel/', ...)
path('facultad/practicas/', ...)
path('facultad/practicas/crear/', ...)
path('facultad/practicas/<int:pk>/editar/', ...)
path('facultad/practicas/<int:pk>/postulantes/', ...)
path('facultad/inscripcion/<int:inscripcion_pk>/evaluar/', ...)
```

### 5. **Templates creados**
```
templates/inscripciones/
├── panel_empresa.html
├── mis_practicas_empresa.html
├── crear_practica.html
├── editar_practica.html
├── postulantes_practica.html
├── evaluar_postulante.html
├── panel_facultad.html
├── mis_practicas_facultad.html
├── crear_practica_interna.html
├── editar_practica_interna.html
├── postulantes_practica_interna.html
└── evaluar_postulante_interno.html
```

### 6. **Base template actualizado**
- Menú dinámico según tipo de usuario
- Opciones específicas para estudiante/empresa/facultad

### 7. **Forms actualizados** (`inscripciones/forms.py`)
- `EmpresaRegistrationForm` - Ahora crea relación con User
- `FacultadRegistrationForm` - Ahora crea relación con User

---

## 📊 MIGRACIONES APLICADAS

```bash
# Migración creada:
inscripciones/migrations/0003_empresa_user_facultad_user.py
  + Add field user to empresa
  + Add field user to facultad

# Estado actual:
✅ 8 empresas con usuario asignado
✅ 5 facultades con usuario asignado
✅ Todas las empresas y facultades pueden iniciar sesión
```

---

## 🎨 DISEÑO Y UX

- 🎨 **Bootstrap 5** para diseño responsivo
- 📊 **Tarjetas de estadísticas** con colores distintivos
- 🎯 **Iconos Bootstrap Icons** para mejor UX
- 📱 **100% Responsive** - funciona en móviles y tablets
- 🎭 **Menú dinámico** según rol del usuario
- ⚡ **Paginación** en listas largas
- 🔍 **Filtros** por estado en todas las listas

---

## ✅ PRÓXIMOS PASOS RECOMENDADOS

1. **Probar todas las funcionalidades:**
   - Iniciar sesión con cada tipo de usuario
   - Crear prácticas como empresa/facultad
   - Postularse como estudiante
   - Evaluar postulantes

2. **Personalizar contenido:**
   - Agregar logos propios a empresas/facultades
   - Crear más prácticas de ejemplo
   - Ajustar textos y descripciones

3. **Producción:**
   - Configurar email para notificaciones
   - Cambiar contraseñas por defecto
   - Configurar servidor de producción

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### Problema: "No tienes un perfil de empresa"
**Solución:** Asegúrate de iniciar sesión con el usuario correcto (`empresa_*` o `facultad_*`)

### Problema: No aparece el menú de empresa/facultad
**Solución:** 
1. Cierra sesión completamente
2. Inicia sesión nuevamente
3. Verifica que el usuario tiene relación con Empresa/Facultad

### Problema: Error al crear práctica
**Solución:** Verifica que todos los campos obligatorios estén llenos, especialmente las fechas

---

## 📞 SOPORTE

Para más información o problemas técnicos, revisar:
- 📄 `REPORTE_VERIFICACION.md` - Reporte técnico de verificación
- 📘 `GUIA_USUARIO_FINAL.md` - Guía para usuarios finales
- 🔧 Logs del servidor en la terminal

---

**¡El sistema está completamente funcional y listo para usar! 🎉**
