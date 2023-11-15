#####################################
#### Ejemplo de datos compuestos ####
#####################################

### Lista ###
# Puedo acceder a cada una de sus posiciones y modificarlas.
una_lista = [ 'dato 1', 425, True, "dato 2"]
print( f"Lista con info sin modificar: {una_lista}")

# Modifico la lista.
una_lista[0] = 'otro dato'
print( f"Lista modificada: {una_lista}")

### Tupla ###
# Es parecido a una lista, pero no se puede modificar.
una_tupla = ('dato 1', 'dato 2', 4.23, False)
print( f'Tupla: {una_tupla}')

### Conjunto ###
# En un conjunto, no puedo acceder a un dato particular porque no tiene indice.
# Adicionalmente, no maneja datos duplicados. En caso de displayar un conjunto que en su definiciòn tiene datos duplicados, solo muestra uno de ellos.
un_conjunto = {'dato 1', 'dato 2', 127, 126, 'dato 2', True, True}
print( f'Conjunto: {un_conjunto}')

### Diccionario ###
# Es como un conjunto, pero se le puede dar un valor particular a posición (pero en realidad esa posición tiene un nombre asignado). Donde cada valor se tiene que separar por coma (',').
# Si se usa la misma key varias veces, se reemplaza con la ultima como en el caso de 'nombre'.
un_diccionario = {
    'nombre' : 'Pepito',
    'apellido' : 'Rodriguez',
    'altura' : 1.65,
    'esta?' : False,
    'nombre' : 'Rigoberto'
}
print( f'Diccionario: {un_diccionario}')

# Para acceder a una posición, tenemos que detallar la 'key' que queremos acceder.
print( f"Una posición del Diccionario: {un_diccionario['altura']}")