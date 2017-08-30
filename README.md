# POD
  Pesquisa e Ordenação de Dados
 
# ORDENAÇÃO SELECT SORT

O algoritmo Select Sort também consome processamento e tempo, e assim, também não é adequado em matrizes e listas muito grandes. Ele trabalha selecionando um elemento como o primeiro da lista, por exemplo. É realizada uma pesquisa na lista para encontrar o valor mínimo e este é então posicionado no lugar do elemento pesquisado. A pesquisa continua procurando o segundo elemento menor (maior que o mínimo e menor que o selecionado). Esta ordenação será crescente. Para obter uma ordenação decrescente, basta operar o algoritmo de maneira contrária. 

# Execução:
     sequence = [13,11,4,7,8,2]
       
     selection_sort(sequence)

    5 [2, 11, 4, 7, 8, 13]
    4 [2, 8, 4, 7, 11, 13]
    3 [2, 7, 4, 8, 11, 13]
    2 [2, 4, 7, 8, 11, 13]
    1 [2, 4, 7, 8, 11, 13]



# ORDENAÇÃO BUBBLE SORT

O algoritmo Bubble Sort consome tempo e processamento. Apesar de simples, não deve ser utilizado com matrizes ou listas muito extensas para evitar lentidão no processamento.

Seu funcionamento é muito simples. O Algoritmo faz um loop (laço) pelos valores da matriz comparando-os e movendo o maior para a posição anterior. Este método cria uma ordenação decrescente. Para criar uma ordenação crescente, o algoritmo deverá mover o maior valor para a posição posterior, após o elemento testado.

# Execução:
     sequence = [13,11,4,7,8,2]
       
     burble_sort(sequence)
     [11, 4, 7, 8, 2, 13]
     [4, 7, 8, 2, 11, 13]
     [4, 7, 2, 8, 11, 13]
     [4, 2, 7, 8, 11, 13]
     [2, 4, 7, 8, 11, 13]
