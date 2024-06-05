from Empleados import *
from os import system



lista_empleados = []
empleado = crear_empleado(1, 35555555, 1000000, "pepe", "grillo", "Gerente")
lista_empleados.append(empleado)
empleado = crear_empleado(2, 35555556, 1000001, "Cornelio", "DelRancho", "Gerente")
lista_empleados.append(empleado)


lista_diccionarios_empleados = [
    {"ID": 1, "Nombre": "Juan", "Apellido": "Pérez", "DNI": "12345678", "Puesto": "Gerente", "Salario": 50000},
    {"ID": 2, "Nombre": "María", "Apellido": "Gómez", "DNI": "87654321", "Puesto": "Asistente", "Salario": 30000},
    {"ID": 3, "Nombre": "Carlos", "Apellido": "López", "DNI": "56781234", "Puesto": "Analista", "Salario": 40000}
]

# Obtener el máximo valor de la clave "ID"
max_id = max(empleado["ID"] for empleado in lista_diccionarios_empleados)

print(max_id)