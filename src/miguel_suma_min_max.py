def suma_valor_min_max(ls1):

    '''
    Esta función devuelve el sumatorio del valor mínimo y máximo de una lista
    '''
    suma=min(ls1)+max(ls1)
    return suma

if __name__ == "__main__":
    print(suma_valor_min_max([4,7,5,3,9]))
