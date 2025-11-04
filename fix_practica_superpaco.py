import os
import django
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_practicas.settings')
django.setup()

from inscripciones.models import Practica
from django.utils import timezone

# Encontrar la práctica de Super Paco que está expirada
practica = Practica.objects.get(id=32, titulo="Ayudante")

print(f"Práctica: {practica.titulo}")
print(f"Empresa: {practica.empresa.nombre}")
print(f"Fecha límite ACTUAL: {practica.fecha_limite_inscripcion}")

# Actualizar las fechas para que la práctica sea válida
nueva_fecha_limite = timezone.now() + timedelta(days=7)
nueva_fecha_inicio = timezone.now() + timedelta(days=10)
nueva_fecha_fin = nueva_fecha_inicio + timedelta(days=practica.duracion_semanas * 7)

print(f"Fecha inicio ACTUAL: {practica.fecha_inicio}")
print(f"Fecha fin ACTUAL: {practica.fecha_fin}")

practica.fecha_limite_inscripcion = nueva_fecha_limite
practica.fecha_inicio = nueva_fecha_inicio
practica.fecha_fin = nueva_fecha_fin
practica.save()

print(f"\n--- FECHAS ACTUALIZADAS ---")
print(f"Fecha límite inscripción: {practica.fecha_limite_inscripcion}")
print(f"Fecha inicio: {practica.fecha_inicio}")
print(f"Fecha fin: {practica.fecha_fin}")
print("\n✅ Práctica actualizada! Ahora aparecerá en la lista de estudiantes.")
