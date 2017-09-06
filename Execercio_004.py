# Escreva um programa em Python que recebe como argumento um polinômio em notação
# algébrica e gera como saída a primeira derivada desse polinômio. Em seguida, calcule a
# função T(n) (modelo simplificado) e faça o estudo do seu desempenho em uma tabela e um
# gráfico.
def poli(lista):
                aux = ""
                for i in range(len(lista)):
                        temp = len(lista) -  1 - i
                        if(temp == 1):
                                aux = aux + " %dx + " %lista[i]
                        elif(temp !=0 and (lista[i] !=0)):
                                aux = aux + "%d" %lista[i] + "x ^ %d + " %temp
                        else:
                        		if lista[i] !=0 :
                        			aux = aux + "%d" %lista[i]       
                        
                        
                        
                return aux




sequence = [1,3,0,0,5,4]
print(poli(sequence))
