Para cada um dos algoritmos a seguir, unique1 e unique2 os quais resolvem o problema da
singularidade de um elemento, executar uma análise experimental do tempo de execução
para determinar o valor maior de n tal que o algoritmo dado execute em um minuto ou
menos. 


def unique1(S):
	"""Return True if there are no duplicate elements in sequence S """
	for j in range(len(S)):
		for k in range(j+1, len(S)):
			if S[j] == S[k]:
				return False
	return True


def unique2(S):
	"""Return True if there are no duplicate elements in sequence S """
	temp = sorted(S)
	for j in range(1, len(temp)):
		if S[j - 1 ] == S[j]:
			return False
	return True