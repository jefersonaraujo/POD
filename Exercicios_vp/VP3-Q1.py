#1) Suponha  que  você tenha um dada  sequência  de  n  elementos,  S,  contendo inteiros distintosque   estão   listados   em   ordem   crescente.   Dado   um   número   k, implementeum   algoritmorecursivo  para  encontrar  dois  inteiros  em  S, tais que  soma seja  igual  a  k,  se  existir tal par

def soma(array,valor,inicial):
    for i in range(len(array)):
        if inicial == i:
            continue
        else:
            temp = array[inicial] + array[i]
            if temp == valor:
                return [array[inicial],array[i]]

    return tentativa(array,valor,inicial+1)
    
array = [0, 1, 2, 3, 4, 6, 7, 9,10,11, 12, 13,14,15]
array = soma(array,29,0)
print(array)

