import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_practicas.settings')
django.setup()

from inscripciones.models import Practica, PracticaInterna
from django.utils import timezone

print("=" * 70)
print("VERIFICACIÓN DE VISIBILIDAD DE PRÁCTICAS PARA ESTUDIANTES")
print("=" * 70)

ahora = timezone.now()
print(f"\nFecha actual: {ahora}\n")

# Prácticas de Empresas
print("🏢 PRÁCTICAS DE EMPRESAS (Prácticas Pre-Profesionales)")
print("-" * 70)
practicas_empresa = Practica.objects.filter(
    activa=True, 
    fecha_limite_inscripcion__gte=ahora
).select_related('empresa')

print(f"Total disponibles: {practicas_empresa.count()}")
for i, p in enumerate(practicas_empresa, 1):
    print(f"\n{i}. {p.titulo}")
    print(f"   Empresa: {p.empresa.nombre}")
    print(f"   Cupos: {p.cupos_disponibles}/{p.cupos_totales}")
    print(f"   Fecha límite: {p.fecha_limite_inscripcion}")
    print(f"   URL: /practicas/{p.pk}/")

# Prácticas Internas
print("\n" + "=" * 70)
print("🎓 PRÁCTICAS INTERNAS (Servicio Comunitario)")
print("-" * 70)
practicas_internas = PracticaInterna.objects.filter(
    activa=True,
    fecha_limite_inscripcion__gte=ahora
).select_related('facultad')

print(f"Total disponibles: {practicas_internas.count()}")
for i, p in enumerate(practicas_internas, 1):
    print(f"\n{i}. {p.titulo}")
    print(f"   Facultad: {p.facultad.nombre}")
    print(f"   Tipo: {p.get_tipo_servicio_display()}")
    print(f"   Cupos: {p.cupos_disponibles}/{p.cupos_totales}")
    print(f"   Fecha límite: {p.fecha_limite_inscripcion}")
    print(f"   URL: /practicas-internas/{p.pk}/")

# Resumen
print("\n" + "=" * 70)
print("RESUMEN")
print("=" * 70)
print(f"✅ Prácticas de Empresas: {practicas_empresa.count()}")
print(f"✅ Prácticas Internas: {practicas_internas.count()}")
print(f"📊 Total visible para estudiantes: {practicas_empresa.count() + practicas_internas.count()}")
print("\n🔗 URLs para acceder:")
print("   - Prácticas de Empresas: http://127.0.0.1:8000/practicas/")
print("   - Prácticas Internas: http://127.0.0.1:8000/practicas-internas/")
print("   - Dropdown en Navbar: 'Prácticas' → Elegir tipo")
print("=" * 70)
