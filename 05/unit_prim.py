import sys

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for coluna in range(vertices)]
					for linha in range(vertices)]

	def printMST(self, parent):
		print("Vértices PRIM \tPeso")
		for i in range(1, self.V): 
			print(parent[i], "-", i, "\t,\t", self.graph[i][parent[i]])

	# Acha o vértice com menor distância, entre os que não fora visitados
	def minKey(self, key, mstSet):

		min = sys.maxsize

		for v in range(self.V):
			if key[v] < min and mstSet[v] == False:
				min = key[v]
				min_index = v

		return min_index

    # Constrói e exibe o MST para um graph representado através da matriz de adjancencia
	def primMST(self):

		# Key usada para escolher valor mínimo
		key = [sys.maxsize] * self.V
		parent = [None] * self.V # Array que armazeno o MST
		# Define como 0 para que esse vértice seja o primeiro
		key[0] = 0
		mstSet = [False] * self.V

		parent[0] = -1 # Primeiro vértice é sempre a raíz

		for cout in range(self.V):

			# Seleciona o vértice de menor distância entre os vértices ainda não selecionados
			# u é igual à raíz na primeira iteração
			u = self.minKey(key, mstSet)

			mstSet[u] = True

			for v in range(self.V):
				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
						key[v] = self.graph[u][v]
						parent[v] = u

		self.printMST(parent)