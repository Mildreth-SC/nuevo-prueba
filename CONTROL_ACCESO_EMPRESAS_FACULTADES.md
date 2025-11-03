# 🔒 CONTROL DE ACCESO: EMPRESAS Y FACULTADES

## ✅ Cambios Implementados

### 1. **Empresas: Publicación de Prácticas** ✅

**Problema anterior:**
- La empresa podía seleccionar cualquier empresa al crear una práctica
- Riesgo de crear prácticas para otras empresas

**Solución implementada:**
- ✅ Eliminado el campo `empresa` del formulario `PracticaForm`
- ✅ La vista `crear_practica_empresa()` asigna automáticamente la empresa del usuario autenticado
- ✅ No hay forma de que una empresa cree prácticas para otra

**Código modificado:**
```python
# inscripciones/forms.py
class PracticaForm(forms.ModelForm):
    class Meta:
        model = Practica
        fields = ['titulo', 'descripcion', ...]  # SIN 'empresa'
```

```python
# inscripciones/views.py
def crear_practica_empresa(request):
    # ...
    practica = form.save(commit=False)
    practica.empresa = empresa  # Asignación automática
    practica.cupos_totales = practica.cupos_disponibles
    practica.save()
```

---

### 2. **Facultades: Publicación de Prácticas Internas** ✅

**Problema anterior:**
- La facultad podía seleccionar cualquier facultad al crear una práctica interna
- Riesgo de crear prácticas internas para otras facultades

**Solución implementada:**
- ✅ Eliminado el campo `facultad` del formulario `PracticaInternaForm`
- ✅ La vista `crear_practica_facultad()` asigna automáticamente la facultad del usuario autenticado
- ✅ No hay forma de que una facultad cree prácticas para otra

**Código modificado:**
```python
# inscripciones/forms.py
class PracticaInternaForm(forms.ModelForm):
    class Meta:
        model = PracticaInterna
        fields = ['titulo', 'descripcion', ...]  # SIN 'facultad'
```

```python
# inscripciones/views.py
def crear_practica_facultad(request):
    # ...
    practica = form.save(commit=False)
    practica.facultad = facultad  # Asignación automática
    practica.cupos_totales = practica.cupos_disponibles
    practica.save()
```

---

### 3. **Empresas y Facultades: Bloqueo de Inscripciones** ✅

**Problema anterior:**
- Empresas y facultades podían intentar inscribirse en prácticas
- Eso no tiene sentido lógico (solo estudiantes deben inscribirse)

**Solución implementada:**

#### A) **Protección a nivel de vista (Backend)**
- ✅ Decorador `@estudiante_required` en `inscribirse_practica()`
- ✅ Si empresa/facultad intenta acceder: mensaje de error y redirección

```python
@estudiante_required
def inscribirse_practica(request, pk):
    # Solo estudiantes pueden acceder a esta vista
    ...
```

#### B) **Protección a nivel de interfaz (Frontend)**
- ✅ Botón "Inscribirse" solo visible para estudiantes
- ✅ Empresas/facultades ven mensaje: "Solo los estudiantes pueden inscribirse"

**Template modificado:**
```django
{% if user.estudiante %}
    <a href="{% url 'inscribirse_practica' practica.pk %}" class="btn btn-primary btn-lg">
        <i class="bi bi-person-plus"></i> Inscribirse
    </a>
{% else %}
    <div class="alert alert-warning">
        <strong>Solo estudiantes</strong>
        <p>Solo los estudiantes pueden inscribirse en prácticas.</p>
    </div>
{% endif %}
```

#### C) **Menú de navegación personalizado**
- ✅ Estudiantes ven: "Mis Inscripciones" y "Mi Perfil"
- ✅ Empresas ven: "Panel de Control", "Mis Prácticas", "Nueva Práctica"
- ✅ Facultades ven: "Panel de Control", "Prácticas Internas", "Nueva Práctica"
- ❌ Empresas/Facultades NO ven opciones de inscripción

---

## 🎯 Flujos de Trabajo Actualizados

### **Flujo: Empresa publica una práctica**

1. Empresa inicia sesión con: `empresa_1790123456001` / `empresa123`
2. Clic en "Nueva Práctica" en el menú
3. Completa formulario (SIN poder elegir empresa)
4. Al guardar:
   - ✅ Sistema asigna automáticamente `practica.empresa = request.user.empresa`
   - ✅ La práctica queda registrada para ESA empresa únicamente
5. Resultado: Práctica visible en "Mis Prácticas" de la empresa

### **Flujo: Facultad publica una práctica interna**

1. Facultad inicia sesión con: `facultad_fci` / `facultad123`
2. Clic en "Nueva Práctica" en el menú
3. Completa formulario (SIN poder elegir facultad)
4. Al guardar:
   - ✅ Sistema asigna automáticamente `practica.facultad = request.user.facultad`
   - ✅ La práctica interna queda registrada para ESA facultad únicamente
5. Resultado: Práctica interna visible en "Prácticas Internas" de la facultad

### **Flujo: Empresa intenta inscribirse (BLOQUEADO)**

1. Empresa ve una práctica en el sistema
2. Clic en "Ver Detalles"
3. Ve toda la información PERO:
   - ❌ NO ve botón "Inscribirse"
   - ✅ Ve mensaje: "Solo los estudiantes pueden inscribirse"
4. Si intenta acceder directamente a la URL `/inscribirse/<id>/`:
   - ❌ Decorador `@estudiante_required` lo bloquea
   - ✅ Mensaje de error: "Necesitas un perfil de estudiante"
   - ✅ Redirección a página de perfil

### **Flujo: Estudiante se inscribe (PERMITIDO)**

1. Estudiante inicia sesión con: `estudiante1` / `estudiante123`
2. Ve una práctica disponible
3. Clic en "Ver Detalles"
4. ✅ Ve botón "Inscribirse" (verde)
5. Completa formulario de inscripción
6. ✅ Inscripción exitosa

---

## 🔐 Niveles de Seguridad

### **Nivel 1: Formulario (UI)**
- Campo empresa/facultad NO existe en el formulario
- Usuario no puede manipular HTML para agregarlo

### **Nivel 2: Vista (Backend)**
- Asignación automática en `form.save(commit=False)`
- Decoradores `@empresa_required` / `@facultad_required`
- Validación de `hasattr(request.user, 'empresa')`

### **Nivel 3: Modelo (Base de datos)**
- Campo `user` con `OneToOneField` (relación única)
- No se puede crear práctica sin empresa/facultad válida

### **Nivel 4: Decorador (Control de acceso)**
```python
@estudiante_required  # Solo estudiantes
@empresa_required     # Solo empresas
@facultad_required    # Solo facultades
```

---

## 📋 Archivos Modificados

### 1. **inscripciones/forms.py**
- ✅ `PracticaForm`: Removido campo `empresa`
- ✅ `PracticaInternaForm`: Removido campo `facultad`

### 2. **templates/inscripciones/detalle_practica.html**
- ✅ Botón "Inscribirse" solo para estudiantes
- ✅ Mensaje de advertencia para empresas/facultades

### 3. **inscripciones/views.py** (Ya estaba bien)
- ✅ `crear_practica_empresa()`: Asigna `practica.empresa = empresa`
- ✅ `crear_practica_facultad()`: Asigna `practica.facultad = facultad`
- ✅ `inscribirse_practica()`: Decorador `@estudiante_required`

### 4. **templates/inscripciones/base.html** (Ya estaba bien)
- ✅ Menú personalizado por tipo de usuario

---

## ✅ Pruebas de Verificación

### **Prueba 1: Empresa crea práctica**
```
1. Login: empresa_1790123456001 / empresa123
2. Ir a: /empresa/practicas/crear/
3. Verificar: Campo "empresa" NO aparece en formulario
4. Crear práctica: "Práctica de Prueba"
5. Verificar: En /empresa/practicas/ aparece con empresa correcta
```

### **Prueba 2: Facultad crea práctica interna**
```
1. Login: facultad_fci / facultad123
2. Ir a: /facultad/practicas/crear/
3. Verificar: Campo "facultad" NO aparece en formulario
4. Crear práctica: "Práctica Interna de Prueba"
5. Verificar: En /facultad/practicas/ aparece con facultad correcta
```

### **Prueba 3: Empresa intenta inscribirse (debe fallar)**
```
1. Login: empresa_1790123456001 / empresa123
2. Ir a: /practicas/1/ (detalle de práctica)
3. Verificar: NO aparece botón "Inscribirse"
4. Verificar: Aparece mensaje "Solo estudiantes"
5. Intentar acceder: /inscribirse/1/
6. Verificar: Error y redirección
```

### **Prueba 4: Estudiante se inscribe (debe funcionar)**
```
1. Login: estudiante1 / estudiante123
2. Ir a: /practicas/1/
3. Verificar: SÍ aparece botón "Inscribirse"
4. Clic en "Inscribirse"
5. Verificar: Formulario de inscripción se muestra
6. Completar y guardar
7. Verificar: Inscripción exitosa en /mis-inscripciones/
```

---

## 🎉 RESULTADO FINAL

✅ **Empresas**: Solo pueden crear y gestionar SUS prácticas  
✅ **Facultades**: Solo pueden crear y gestionar SUS prácticas internas  
✅ **Estudiantes**: Solo ellos pueden inscribirse en prácticas  
✅ **Seguridad**: Múltiples capas de protección (UI + Backend + DB)  
✅ **UX**: Mensajes claros según rol de usuario  

---

**Sistema completamente seguro y lógico.** 🔒✨
