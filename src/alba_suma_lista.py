def suma_lista(lista):
    '''
    Función que devuelve la suma de todos los elementos de una lista
    '''
    suma = 0
    for num in lista:
        suma = suma + num 
    return suma

suma_lista([2, 4, 9, 3, 9])