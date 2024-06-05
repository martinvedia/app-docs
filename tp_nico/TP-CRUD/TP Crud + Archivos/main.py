"""""
Nombre: Nicolás
Apellido: Doyhenart

TP Recursos Inhumanos CRUD
"""""
from Empleados import *
from os import system

def elegir_opcion():
    opcion = input("""Bienvenido a Recursos Inhumanos\nElija una opción:\n1. Ingresar empleado\n2. Modificar empleado\n3. Eliminar empleado\n4. Mostrar todos\n5. Calcular salario promedio\n6. Buscar empleado por DNI\n7. Ordenar empleados\n8. Salir
""")
    
    return opcion

lista_empleados = []

system("cls")

while True:
    opcion = elegir_opcion()
    match opcion:
        case "1":
            ingresar_empleados(lista_empleados)
        case "2":
            modificar_empleado(lista_empleados)
        case "3":
            eliminar_empleado(lista_empleados)
        case "4":
            system("cls")
            mostrar_todos(lista_empleados)
        case "5":
            calcular_promedio(lista_empleados)
        case "6":
            buscar_emp_dni(lista_empleados)
        case "7":
            ordenar_empleados(lista_empleados)
        case "8":
            print("Gracias por utilizar el programa..")
            break
    
    system("pause")
    system("cls")