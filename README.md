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



# ALGORITMO MERGE SORT

A idéia básica do Merge Sort é criar uma sequência ordenada a partir de duas outras também ordenadas.
Para isso, o algoritmo Merge Sort divide a sequência original em pares de dados, agrupa estes pares na ordem desejada; depois as agrupa as sequências de pares já ordenados, formando uma nova sequência ordenada de quatro elementos, e assim por diante, até ter toda a sequência ordenada.
Algoritmo:
  Os três passos úteis dos algoritmos dividir-para-conquistar, que se aplicam ao Merge Sort são:
  Dividir: Dividir os dados em subsequências pequenas;
  Este passo é realizado recursivamente, iniciando com a divisão do vetor de n elementos em duas metades, cada uma das metades é           novamente dividida em duas novas metades e assim por diante, até que não seja mais possível a divisão (ou seja, sobrem n vetores com     um elemento cada).
  
  Conquistar: Classificar as duas metades recursivamente aplicando o merge sort;

  Combinar: Juntar as duas metades em um único conjunto já classificado.

  Para completar a ordenação do vetor original de n elementos, faz-se o merge ou a fusão dos sub-vetores já ordenados.
  A desvantagem do Merge Sort é que requer o dobro de memória, ou seja, precisa de um vetor com as mesmas dimensões do vetor que está     sendo classificado.
# Execução:
    sequence = [13,11,4,7,8,2]
    merge_sort(sequence)

      Splitting  [13, 11, 4, 7, 8, 2]
      Splitting  [13, 11, 4]
      Splitting  [13]
      Merging  [13]
      Splitting  [11, 4]
      Splitting  [11]
      Merging  [11]
      Splitting  [4]
      Merging  [4]
      Merging  [4, 11]
      Merging  [4, 11, 13]
      Splitting  [7, 8, 2]
      Splitting  [7]
      Merging  [7]
      Splitting  [8, 2]
      Splitting  [8]
      Merging  [8]
      Splitting  [2]
      Merging  [2]
      Merging  [2, 8]
      Merging  [2, 7, 8]
      Merging  [2, 4, 7, 8, 11, 13]

