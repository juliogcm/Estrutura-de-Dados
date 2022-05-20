class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vértice \t Dist da Origem")
        for node in range(self.V):
            print(node, "\t\t", dist[node])
 
    def minDistance(self, dist, sptSet):
 
        # Inicializa as distancias mínimas
        min = 1e7
 
        # Analise dos vertices
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    def dijkstra(self, src):
 
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            #Seleciona o vértice de menor distância dos não visitados.
            u = self.minDistance(dist, sptSet)
 
            # Coloca o vértice de menor distancia na árvore do caminho mínimo
            sptSet[u] = True

            #Atualiza o valor da distancia dos vertices adjacentes do vertice escolhido
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(dist)