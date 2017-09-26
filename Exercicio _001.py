import random
import time

def performance():
    n = 1024
    array =[]

    while n < 50000:
        for r in range(n):
            i = random.randint(0,n)
        print(i)
        array.append(i)
        begin = float(time.time())
        array.reverse()
        end = float(time.time())
        print(n, '  ',(end - begin) *1000000)
        n = n * 2



def invert(lista):
    for x in lista[::-1]:
        listaIve=[]
        listaIve.append(x)
        print(listaIve)
    
    


lista = [1,2,3,4,5]
invert(lista)

performance()
