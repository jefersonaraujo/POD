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

##### Algoritmo:
  Os três passos úteis dos algoritmos dividir-para-conquistar, que se aplicam ao Merge Sort são:
  > Dividir: Dividir os dados em subsequências pequenas;
  > Este passo é realizado recursivamente, iniciando com a divisão do vetor de n elementos em duas metades, cada uma das metades é           novamente dividida em duas novas metades e assim por diante, até que não seja mais possível a divisão (ou seja, sobrem n vetores com     um elemento cada).
  
  > Conquistar: Classificar as duas metades recursivamente aplicando o merge sort;

  > Combinar: Juntar as duas metades em um único conjunto já classificado.

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
      
# ALGORITMO QUICK SORT

Determina-se um elemento pivô. O pivô é posicionado dentro do vetor de tal forma que, todos à esquerda do pivô são menores que ele e, todos à direita do pivô são maiores. O pivô "divide" o vetor em dois subvetores.
Recursivamente o quick sort é realizado na primeira metade do vetor e na segunda metade.

Algoritmo: Seja x o vetor a ser ordenado e n o número de elementos de x. Seja a um elemento de x escolhido ao acaso (por exemplo, a=x[0]). Suponha que os elementos de x estão divididos de tal forma que a é colocado na posição j e as seguintes condições são verdadeiras:

  >Todos os elementos nas posições de 0 a j-1 são menores que a.
  
  >Todos os elementos nas posições de j+1 a n-1 são maiores ou iguais a a.  
  
 # Execução:
    sequence = [13,11,4,7,8,2]
    quick_sort(sequence)
    [2, 11, 4, 7, 8, 13]
    [2, 11, 4, 7, 8, 13]
    [2, 8, 4, 7, 11, 13]
    [2, 7, 4, 8, 11, 13]
    [2, 4, 7, 8, 11, 13]


# ALGORITMO RADIX  
  Consiste em dividir os elementos do vetor a ser ordenado em baldes, ordenando primeiramente o conteúdo dos baldes, e depois agrupando   os elementos.
  
  - Melhor caso, Complexidade Linear, O(n). 
  - Pior caso, Quadrático,O(n²). 
  
 #### Vantagens:
  - Não realiza comparações
  - É estável, preserva a ordem de chaves iguais
  - Tempo Linear 

 #### Desvantagens:
  - Precisa de mais memória para ordenar o conjunto
  - O algoritmo se torna muito caro quando o vetor chave é muito extenso

  
  
## EXERCÍCIO 001
##### Escreva uma função em Python que reverte a ordem de uma lista de n inteiros. Em seguida,calcule a função T(n)  (modelo simplificado) e faça o estudo comparativo em uma tabela egráfico do desempenho de sua função versus o método nativo fornecido pela linguagem.

## EXERCÍCIO 002
#####  Escreva uma classe em Python contendo um método que recebe dois arrays (de tamanho n)a e b contendo valores inteiros e calcula o produto de a por b. Sendo assim, seu métododeve retornar um novo array c, tal que c[i] = a[i] * b[i], para i = 0, ..., n-1. Faça o estudocomparativo em uma tabela e gráfico do desempenho de seu código.

## EXERCÍCIO 003
##### Escreva um programa em Python que recebe como argumento um polinômio em notaçãoalgébrica e gera como saída a primeira derivada desse polinômio. Em seguida, calcule afunção T(n)  (modelo simplificado) e faça o estudo do seu desempenho em uma tabela e umgráfico.

## EXERCÍCIO 004
##### Escreva um programa em Python para encontrar o mínimo e máximo elementos de um dadoarray de tamanho n usando menos que  3n/2  comparações. (Dica: Primeiro, construa umgrupo de mínimos candidatos e outro de máximos candidatos)


## EXERCÍCIO 005
##### Para cada um dos algoritmos a seguir, unique1 e unique2 os quais resolvem o problema dasingularidade de um elemento, executar uma análise experimental do tempo de execuçãopara determinar o valor maior de n tal que o algoritmo dado execute em um minuto oumenos.

## EXERCÍCIO 006
##### Suponha que temos uma sequência de n elementos S tal que cada elemento em S representaum voto diferente para presidente, onde cada voto é dado como um inteiro que representaum   determinado   candidato.   Projetar   um   algoritmo   com  O (n log n)  de   tempo   decomplexidade para ver quem ganha a eleição S, assumindo que ganha o candidato com maisvotos.

## EXERCÍCIO 007
##### Implementar uma versão in-place de insertion-sort e uma versão in-place do selection-sort.Execute  testes  de  benchmarking  para  determinar  o intervalo  de  valores   de  n onde  qselection-sort é, em média, melhor do que a insertion-sort
