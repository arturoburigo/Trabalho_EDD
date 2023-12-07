import numpy as np
import sys

class Dijkstra:
    def __init__(self, vertices, arestas, inicio):
        self.tamanho = len(vertices)
        self.vertices = vertices
        self.grafo = arestas
        self.inicio = inicio
    
    def mostra_solucao(self, distancias):
        print('Menores distâncias de {} até todos os outros'.format(self.vertices[self.inicio]))
        for vertice in range(self.tamanho):
            print(self.vertices[vertice], distancias[vertice])
    
    def distancia_minima(self, distancia, visitados):
        minimo = sys.maxsize
        for vertice in range(self.tamanho):
            if distancia[vertice] < minimo and not visitados[vertice]:
                minimo = distancia[vertice]
                indice_minimo = vertice
        return indice_minimo
    
    def dijkstra(self):
        distancia = [sys.maxsize] * self.tamanho
        distancia[self.inicio] = 0
        visitados = [False] * self.tamanho
        
        for _ in range(self.tamanho):
            indice_minimo = self.distancia_minima(distancia, visitados)
            visitados[indice_minimo] = True
            
            for vertice in range(self.tamanho):
                if (self.grafo[indice_minimo][vertice] > 0 and 
                    not visitados[vertice] and 
                    distancia[vertice] > distancia[indice_minimo] + self.grafo[indice_minimo][vertice]):
                    
                    distancia[vertice] = distancia[indice_minimo] + self.grafo[indice_minimo][vertice]
        
        self.mostra_solucao(distancia)

# Exemplo de utilização:
cidades = {
    0: 'SC', 1: 'AL', 2: 'AP', 3: 'AM', 4: 'BA', 5: 'CE', 6: 'DF', 7: 'ES',
    8: 'GO', 9: 'MA', 10: 'MT', 11: 'MS', 12: 'MG', 13: 'PA', 14: 'PB',
    15: 'PR', 16: 'PE', 17: 'PI', 18: 'RJ', 19: 'RN'
}

vertices = {'SC': 0, 'AL': 1, 'AP': 2, 'AM': 3, 'BA': 4, 'CE': 5, 'DF': 6,
            'ES': 7, 'GO': 8, 'MA': 9, 'MT': 10, 'MS': 11, 'MG': 12, 'PA': 13,
            'PB': 14, 'PR': 15, 'PE': 16, 'PI': 17, 'RJ': 18, 'RN': 19}


arestas = np.zeros([len(cidades), len(cidades)], dtype=int)

arestas[vertices['SC'], vertices['AL']] = 9
arestas[vertices['AL'], vertices['SC']] = 9

arestas[vertices['AL'], vertices['CE']] = 13
arestas[vertices['CE'], vertices['AL']] = 13

arestas[vertices['AL'], vertices['MS']] = 5
arestas[vertices['MS'], vertices['AL']] = 5

arestas[vertices['CE'], vertices['AP']] = 20
arestas[vertices['AP'], vertices['CE']] = 20

arestas[vertices['CE'], vertices['DF']] = 13
arestas[vertices['DF'], vertices['CE']] = 13

arestas[vertices['MS'], vertices['DF']] = 20
arestas[vertices['DF'], vertices['MS']] = 20

arestas[vertices['MS'], vertices['RN']] = 4
arestas[vertices['RN'], vertices['MS']] = 4

arestas[vertices['DF'], vertices['BA']] = 1
arestas[vertices['BA'], vertices['DF']] = 1

arestas[vertices['DF'], vertices['ES']] = 11
arestas[vertices['ES'], vertices['DF']] = 11

arestas[vertices['RN'], vertices['ES']] = 34
arestas[vertices['ES'], vertices['RN']] = 34

arestas[vertices['AP'], vertices['AM']] = 3
arestas[vertices['AM'], vertices['AP']] = 3

arestas[vertices['AM'], vertices['PE']] = 25
arestas[vertices['PE'], vertices['AM']] = 25

arestas[vertices['AM'], vertices['BA']] = 7
arestas[vertices['BA'], vertices['AM']] = 7

arestas[vertices['BA'], vertices['PR']] = 12
arestas[vertices['PR'], vertices['BA']] = 12

arestas[vertices['PE'], vertices['PR']] = 3
arestas[vertices['PR'], vertices['PE']] = 3

arestas[vertices['PR'], vertices['MT']] = 1
arestas[vertices['MT'], vertices['PR']] = 1

arestas[vertices['PR'], vertices['MA']] = 19
arestas[vertices['MA'], vertices['PR']] = 19

arestas[vertices['MT'], vertices['PI']] = 23
arestas[vertices['PI'], vertices['MT']] = 23

arestas[vertices['PI'], vertices['MG']] = 24
arestas[vertices['MG'], vertices['PI']] = 24

arestas[vertices['MG'], vertices['MA']] = 63
arestas[vertices['MA'], vertices['MG']] = 63

arestas[vertices['MA'], vertices['GO']] = 17
arestas[vertices['GO'], vertices['MA']] = 17

arestas[vertices['GO'], vertices['RJ']] = 16
arestas[vertices['RJ'], vertices['GO']] = 16

arestas[vertices['GO'], vertices['PA']] = 7
arestas[vertices['PA'], vertices['GO']] = 7

arestas[vertices['PA'], vertices['PB']] = 19
arestas[vertices['PB'], vertices['PA']] = 19

arestas[vertices['PB'], vertices['ES']] = 11
arestas[vertices['ES'], vertices['PB']] = 11

arestas[vertices['ES'], vertices['RJ']] = 6
arestas[vertices['RJ'], vertices['ES']] = 6



dijkstra = Dijkstra(cidades, arestas, 0)  # 0 é o índice da cidade inicial
dijkstra.dijkstra()
