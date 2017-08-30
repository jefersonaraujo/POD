# POD
  Pesquisa e Ordenação de Dados
 
# ORDENAÇÃO SELECT SORT

O algoritmo Select Sort também consome processamento e tempo, e assim, também não é adequado em matrizes e listas muito grandes. Ele trabalha selecionando um elemento como o primeiro da lista, por exemplo. É realizada uma pesquisa na lista para encontrar o valor mínimo e este é então posicionado no lugar do elemento pesquisado. A pesquisa continua procurando o segundo elemento menor (maior que o mínimo e menor que o selecionado). Esta ordenação será crescente. Para obter uma ordenação decrescente, basta operar o algoritmo de maneira contrária. 

Execulção:
       sequence = [13,11,4,7,8,2]
       
     selection_sort(sequence)

    5 [2, 11, 4, 7, 8, 13]
    4 [2, 8, 4, 7, 11, 13]
    3 [2, 7, 4, 8, 11, 13]
    2 [2, 4, 7, 8, 11, 13]
    1 [2, 4, 7, 8, 11, 13]
