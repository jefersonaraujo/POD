# Escreva um programa em Python que recebe como argumento um polinômio em notação
# algébrica e gera como saída a primeira derivada desse polinômio. Em seguida, calcule a
# função T(n) (modelo simplificado) e faça o estudo do seu desempenho em uma tabela e um
# gráfico.
def poli(lista):
                aux = ""
                derivada = ""
                polinomio = "f(x) = "
                for i in range(len(lista)):
                        exp = len(lista) -  1 - i

                        if(exp == 1):
                                aux = aux + " %dx + " %lista[i]
                                derivada = derivada + " %d + " %(lista[i] * exp)

                                
                        elif(exp !=0 and (lista[i] !=0)):

                                aux = aux + "%d" %lista[i] + "x ^ %d + " %exp
                                if i == 0 :
                                	expAux = exp -i -1
                                else:
                                	expAux = exp - i
                                	
                                derivada = derivada + "%d" %(lista[i] * exp) + "x ^ %d + " %(expAux)
                        else:
                        		if lista[i] !=0 :
                        			aux = aux + "%d" %lista[i]
                        			derivada = derivada + "%d" %(lista[i] * exp)       
                					
                		#Tirar Primeira derivada

                polinomio = polinomio + aux 
                derivada = "der(x) = " + derivada
                        
                        
                return polinomio,derivada




sequence = [1,3,0,0,5,4]
teste = poli(sequence)
print (teste[0]) # poli
print (teste[1]) # der

