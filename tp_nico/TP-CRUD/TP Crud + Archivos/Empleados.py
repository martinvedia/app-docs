"""""
Nombre: Nicolás
Apellido: Doyhenart

TP Recursos Inhumanos CRUD
"""""
def crear_empleado(id: int, nombre: str, apellido: str, dni: int, puesto: str, salario: int) -> dict:
    diccionario_empleado = {
        "ID": id,
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Puesto": puesto,
        "Salario": salario,
    }

    return diccionario_empleado

def ingresar_empleados(lista_empleados: list)-> None:
    if len(lista_empleados) == 0:
        id = 1
    else:
        max_id = max(empleado["ID"] for empleado in lista_empleados)
        id = max_id + 1
       
    while len(lista_empleados) < 20:
        
        nombre = input("Ingrese su nombre: ").capitalize()
        while len(nombre) > 20 or not nombre.isalpha():
            print("ERROR")
            nombre = input("Ingrese un nombre válido: ").capitalize()

        apellido = input("Ingrese su apellido: ").capitalize()
        while len(apellido) > 20 or not apellido.isalpha():
            print("ERROR")
            apellido = input("Ingrese un apellido válido: ").capitalize()
        
        dni = int(input("Ingrese su DNI: "))
        while dni <= 5000000 or dni >=  99999999:
            print("ERROR")
            dni = int(input("Ingrese un DNI valido: "))
        
        salario = int(float(input("Ingrese su salario: ")))
        while salario <= 234315:
            print("ERROR")
            salario = int(float(input("Ingrese un salario valido: ")))

        puesto = input("Ingrese su puesto: ").capitalize()
        while puesto not in ["Gerente", "Supervisor", "Analista", "Encargado", "Asistente"]:
            print("ERROR")
            puesto = input("Ingrese un puesto correcto: ").capitalize()
        
        empleado = crear_empleado(id, dni, salario, nombre, apellido, puesto)
        lista_empleados.append(empleado)
        
        if len(lista_empleados) >= 20:
            print("Se ha alcanzado el límite de empleados.")
            break
        
        continuar = input("¿Desea ingresar otro empleado? (si/no): ")
        if continuar.lower() != 'si':
            break



def modificar_empleado(lista_empleados: list[dict]):
    ID_empleado = int(input("Ingrese el ID del empleado a modificar: "))
    bandera_ingreso = False
    modificaciones = False
    
    while True:
        for empleado in lista_empleados:
            if empleado["ID"] == ID_empleado:
                print("¡Empleado existente!")
                bandera_ingreso = True
                opcion_modificar = input("""¿Que desea mofidicar?\n1-Nombre\n2-Apellido\n3-DNI\n4-Puesto\n5-Salario\n6-Ninguno de los anteriores\nElija una opción: """)
                break
            
        match opcion_modificar:
            case "1":
                nuevo_nombre = input("Ingrese el nuevo nombre: ").capitalize()
                while len(nuevo_nombre) > 20 or not nuevo_nombre.isalpha():
                    print("ERROR")
                    nuevo_nombre = input("Ingrese un nombre válido: ").capitalize()
                empleado["Nombre"] = nuevo_nombre
                modificaciones = True
                          
            case "2":
                nuevo_apellido = input("Ingrese el nuevo apellido: ").capitalize()
                while len(nuevo_apellido) > 20 or not nuevo_apellido.isalpha():
                    print("ERROR")
                    nuevo_apellido = input("Ingrese un apellido válido: ").capitalize()
                empleado["Apellido"] = nuevo_apellido
                modificaciones = True
                
            case "3":
                nuevo_dni = int(input("Ingrese el nuevo DNI: "))
                while nuevo_dni <=  5000000 or nuevo_dni >=  99999999:
                    print("ERROR")
                    nuevo_dni = int(input("Ingrese un DNI válido: "))
                empleado["DNI"] = nuevo_dni
                modificaciones = True

            case "4":
                nuevo_puesto = input("Ingrese el nuevo puesto: ").capitalize()
                while nuevo_puesto not in ["Gerente", "Supervisor", "Analista", "Encargado", "Asistente"]:
                    print("ERROR")
                    nuevo_puesto = input("Ingrese un puesto válido: ").capitalize()
                empleado["Puesto"] = nuevo_puesto
                modificaciones = True
                
            case "5":
                    nuevo_salario = int(float(input("Ingrese el nuevo salario: ")))
                    while nuevo_salario <= 234315:
                        print("ERROR")
                        nuevo_salario = int(float(input("Ingrese un salario válido: ")))
                    empleado["Salario"] = nuevo_salario
                    modificaciones = True

            case "6":
                if modificaciones:
                    print("Se realizaron modificaciones.")
                else:
                    print("No se realizaron modificaciones.")
                return modificaciones
        
        continuar = input("¿Desea modificar otro dato? (si/no): ")
        if continuar.lower() != 'si':
            break

    if not bandera_ingreso:
        print("Empleado inexistente")

def eliminar_empleado (lista_empleado: list[dict]):
    ID_emp_eliminado = int(input("Ingrese el ID del empleado que desea eliminar: "))
    empleado_eliminado = None
    for empleado in lista_empleado:
        if empleado["ID"] == ID_emp_eliminado:
            print("Empleado encontrado y eliminado")
            empleado_eliminado = empleado

    if empleado_eliminado != None:
        lista_empleado.remove(empleado_eliminado)

        return empleado_eliminado

    else:
        print("Empleado inexistente")

def mostrar_empleado(empleado: list[dict]):
    print("***********************************************************************")
    encabezado = "      ID       Nombre      Apellido       DNI       Puesto      Salario"
    print(encabezado)
    print(f"{empleado['ID']:>10}{empleado['Nombre']:>12}{empleado['Apellido']:>12}{empleado['DNI']:>12}{empleado['Puesto']:>12}{empleado['Salario']:>12}")
    print("***********************************************************************")

def mostrar_todos(lista_empleados: list[dict]):
    for empleado in lista_empleados:
        mostrar_empleado(empleado)

def calcular_promedio(lista_empleados):
    contador_salarios = 0
    total_empleados = len(lista_empleados)

    for empleado in lista_empleados:
        contador_salarios += empleado["Salario"]

    if total_empleados > 0:
        promedio = contador_salarios / total_empleados
        print(f"El promedio entre los salarios es: ${promedio}")
    else:
        print("ERROR")
        print("No hay empleados en la lista.")

def buscar_emp_dni(lista_empleados: list):
    dni_empleado = int(input("Ingrese el DNI del empleado solicitado: "))
    while True:
        for empleado in lista_empleados:
            if empleado["DNI"] == dni_empleado:
                print("¡Empleado existente!")
                print("***********************************************************************")
                encabezado = "      ID       Nombre      Apellido       DNI       Puesto      Salario"
                print(encabezado)
                print(f"{empleado['ID']:>10}{empleado['Nombre']:>12}{empleado['Apellido']:>12}{empleado['DNI']:>12}{empleado['Puesto']:>12}{empleado['Salario']:>12}")
                print("***********************************************************************")
                break

            else:
                print("Empleado inexistente.")
                break

def ordenar_lista_ascendente(lista_empleados: list[dict], key):
    n = len(lista_empleados)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_empleados[j][key] > lista_empleados[j+1][key]:
                lista_empleados[j], lista_empleados[j+1] = lista_empleados[j+1], lista_empleados[j]

def ordenar_lista_descendente(lista_empleados: list[dict], key):
    n = len(lista_empleados)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_empleados[j][key] < lista_empleados[j+1][key]:
                lista_empleados[j], lista_empleados[j+1] = lista_empleados[j+1], lista_empleados[j]

def ordenar_empleados(lista_empleados: list[dict]):
    while True:
            opcion = input("""¿Como desea ordenar los datos?\n1-Nombre\n2-Apellido\n3-Salario\nElija una opción: """)
            
            match opcion:
                    case "1":
                        opcion_asc_desc = input("Ingrese de que manera quiere ordenar\n1- Ascendente\n2- Descendente: ")
                        match opcion_asc_desc:
                            case "1":
                                ordenar_lista_ascendente(lista_empleados, "Nombre")
                            case "2":
                                ordenar_lista_descendente(lista_empleados, "Nombre")
                    case "2":
                        opcion_asc_desc = input("Ingrese de que manera quiere ordenar\n1- Ascendente\n2- Descendente: ")
                        match opcion_asc_desc:
                            case "1":
                                ordenar_lista_ascendente(lista_empleados, "Apellido")
                            case "2":
                                ordenar_lista_descendente(lista_empleados, "Apellido")
                    case "3":
                        opcion_asc_desc = input("Ingrese de que manera quiere ordenar\n1- Ascendente\n2- Descendente: ")
                        match opcion_asc_desc:
                            case "1":
                                ordenar_lista_ascendente(lista_empleados, "Salario")
                            case "2":
                                ordenar_lista_descendente(lista_empleados, "Salario")
            break
    
############################################################################################################################
##                                         ARCHIVOS                                                                       ##
############################################################################################################################
import re
from datetime import datetime

id = [1,2,3,4,5,6]
nombre = ["Walter","Matias","Ignacio","Sebastian","Federico","Ramon"]
apellidos = ["Perez","Gomez","Pussetto","Meza","Fattori","Abila"]
dni = [4691613,4890013,3291713,3696660,2635611,4034561]
puesto = ["Supervisor","Encargado","Gerente","Analista","Asistente","Asistente"]
salario = [300000,500000,475000,900000,250000,250000]

with open("Empleados.csv", "w") as archivo:
    for i in range (len(salario)):
        registro = f"{id[i]},{nombre[i]},{apellidos[i]},{dni[i]},{puesto[i]},{salario[i]}\n"
        archivo.write(registro)

def leer_empleado(lista_empleado: list):
    with open ("Empleados.csv", "r") as archivo:
        for linea in archivo:
            registro = re.split(",|\n", linea)
            diccionario_empleado = {
                "ID": int(registro[0]),
                "Nombre": registro[1],
                "DNI": int(registro[2]),
                "Puesto": registro[3],
                "Salario": int(registro[4])
            }
        
            lista_empleado.append(diccionario_empleado)