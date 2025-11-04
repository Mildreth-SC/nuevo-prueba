import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_practicas.settings')
django.setup()

from inscripciones.models import Practica
from django.utils import timezone

print("=" * 60)
print("VERIFICACIÓN DE PRÁCTICAS")
print("=" * 60)

todas = Practica.objects.all()
print(f"\nTotal de prácticas: {todas.count()}")

activas = Practica.objects.filter(activa=True)
print(f"Prácticas activas: {activas.count()}")

ahora = timezone.now()
print(f"\nFecha actual: {ahora}")

disponibles = Practica.objects.filter(activa=True, fecha_limite_inscripcion__gte=ahora)
print(f"\nPrácticas disponibles para inscripción: {disponibles.count()}")

print("\n" + "=" * 60)
print("DETALLE DE TODAS LAS PRÁCTICAS:")
print("=" * 60)

for p in todas:
    estado = "✓ ACTIVA" if p.activa else "✗ INACTIVA"
    limite = p.fecha_limite_inscripcion
    if limite >= ahora:
        fecha_estado = "✓ VIGENTE"
    else:
        fecha_estado = f"✗ EXPIRADA (hace {(ahora - limite).days} días)"
    
    print(f"\n{p.id}. {p.titulo}")
    print(f"   Empresa: {p.empresa.nombre}")
    print(f"   Estado: {estado}")
    print(f"   Fecha límite: {limite} - {fecha_estado}")
    print(f"   Cupos: {p.cupos_disponibles}/{p.cupos_totales}")

print("\n" + "=" * 60)
