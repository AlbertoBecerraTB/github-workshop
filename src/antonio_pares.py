def antonio_pares(ls):
    '''
    Función para saber números pares
    
    '''
    
    ls1=[]
    for i in ls:
        if i %2==0:
            ls1.append(i)
    return ls1
antonio_pares([1,2,3,4,5])
        