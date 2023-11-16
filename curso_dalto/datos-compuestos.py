#####################################
#### Ejemplo de datos compuestos ####
#####################################

### Lista ###
# Puedo acceder a cada una de sus posiciones y modificarlas.
unaLista = [ 'dato 1', 425, True, "dato 2"]
print( f"Lista con info sin modificar: {unaLista}")

# Modifico la lista.
unaLista[0] = 'otro dato'
print( f"Lista modificada: {unaLista}")

### Tupla ###
# Es parecido a una lista, pero no se puede modificar.
unaTupla = ('dato 1', 'dato 2', 4.23, False)
print( f'Tupla: {unaTupla}')

### Conjunto ###
# En un conjunto, no puedo acceder a un dato particular porque no tiene indice.
# Adicionalmente, no maneja datos duplicados. En caso de displayar un conjunto que en su definiciòn tiene datos duplicados, solo muestra uno de ellos.
unConjunto = {'dato 1', 'dato 2', 127, 126, 'dato 2', True, True}
print( f'Conjunto: {unConjunto}')

### Diccionario ###
# Es como un conjunto, pero se le puede dar un valor particular a posición (pero en realidad esa posición tiene un nombre asignado). Donde cada valor se tiene que separar por coma (',').
# Si se usa la misma key varias veces, se reemplaza con la ultima como en el caso de 'nombre'.
unDiccionario = {
    'nombre' : 'Pepito',
    'apellido' : 'Rodriguez',
    'altura' : 1.65,
    'esta?' : False,
    'nombre' : 'Rigoberto'
}
print( f'Diccionario: {unDiccionario}')

# Para acceder a una posición, tenemos que detallar la 'key' que queremos acceder.
print( f"Una posición del Diccionario: {unDiccionario['altura']}")

### Función type ###
# Esta funcioon devuelve el tipo de variable
print('type(4): ', type(4))
print('type(4.23): ', type(4.23))
print('type(unaLista): ', type(unaLista))
print('type(unDiccionario): ', type(unDiccionario))
