### Metodos de Listas ###
#########################

unaLista = ['hola', 'como', 'estas']

### Metodos de listas ###
# len -> longitus de la lista
print('len: ', len(unaLista))

# apend -> Agrega elementos a la lista
unaLista.append("capo?")
print(f'unaLista.append("capo?"): {unaLista}')
print('len: ', len(unaLista))

# insert -> Inserta un elemento en una lista en la posición deseada, desplazando todo lo demas
unaLista.insert(3, 'fiera')
print(f'unaLista.insert(2, "fiera"): {unaLista}')

# extend -> Agrega una lista a la lista deseada
unaLista.extend(['otra', 'lista'])
print(f'unaLista.extend(["otra", "lista"]): {unaLista}')
print('len: ', len(unaLista))

# pop -> Quita un elemento detallado en al posiciòn enviada por paràmetro
#        Si se pasa un elemento negativo para para atras -1 -> ultimo -2 -> ante-ultimo
unaLista.pop(3)
print(f'unaLista.pop(4): {unaLista}')
print('len: ', len(unaLista))    

# remove -> Elimina un elemento de la lista, pero por valor, si no encuentra, genera una exception
unaLista.remove('hola')
print(f'unaLista.remove("hola"): {unaLista}')
print('len: ', len(unaLista))    

# sort -> ordena los elementos de una lista, pero no funciona si tiene cadenas y numeros
unaLista.sort()
print(f'unaLista.sort(): {unaLista}')

# clear -> Elimina todos los elementos de la lista
unaLista.clear()
print(f'unaLista.clear(): {unaLista}')
print('len: ', len(unaLista))    