### Metodos cadenas ###
#######################

### Comando "dir" ###
# Esta funcion devuelve todos los metodos que se le pueden aplicar a un objeto
print(dir(4.24))
print('###############################################################################')

### Metodos ###
# Los metodos se invocan como <objeto>.metodo()
# En este caso usamos 'upper' que convierte un string a mayusculas y existen otros como:
    # upper -> Convierte a mayusculas
    # lower -> Convierte a minuscualas
    # capitalize -> Convierte todo a minusculas y la primer retra a mayusculas
    # find -> Devuelve la primer posición encontrada del valor a buscar, sino, devuelve -1
    # index -> Funciona como el find, pero si no encuentra devuelve una excepción
    # isnumeric -> Devuelve True en caso de que el valor sea númerico
    # isalpha -> Devuelve True en caso de que la variable tenga valores entre a y z (si tiene caracteres especiales como espacios o numeros devuelve false)
    # count -> Devuelve la cantidad de veces que encuentra un valor en una cadena
    # len -> Devuelve la cantidad de caracteres que tiene una cadena (guarda que no es un metodo, es una función) -> se invoca como len(<var>)
    # startwith -> Devuelve True en caso de que la cadena comience con el caracter que le pasamos por parámetro
    # endwith -> Lo contario a startwith
    # replace -> Reemplaza lo detallado en la cadena por el otro valor pasado
    # split -> Separa una cadena en una lista utilizando el caracter enviado por parametro (hola,como,estas) -> ['hola', 'como', 'estas']
unString = 'Soy un String'
print(unString.upper()) # SOY UN STRING
print(unString.capitalize()) # Soy un string
print(unString.lower()) # soy un string
print(unString.find('S')) # 0
print(unString.find('Z')) # -1
print(unString.index('o')) # 1
#print(unString.index('Z')) # exception!! 


