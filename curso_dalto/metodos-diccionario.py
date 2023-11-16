### Metodos Diccionario ###
###########################

unDiccionario = {
    'nombre' : 'Rigoberto',
    'apellido' : 'Botico',
    'alturaEnCMs' : 10,
    'marca' : 'Pepito'
}

# keys -> Obtiene un objetivo tipo 'dict_item'
clavesDelDiccionario = unDiccionario.keys()
print(f'Claves del diccionario: {clavesDelDiccionario}')

# set -> Devuelve el valor de una clave:
print(f'Busco el valor de nombre: {unDiccionario.get("alturaEnCMs")}')

# pop -> Elimina un elemento del diccionario (por clave)
print(f'Diccionario antes de borrar: {unDiccionario}')
unDiccionario.pop('marca')
print(f'Diccionario donde se borró la clave marca: {unDiccionario}')