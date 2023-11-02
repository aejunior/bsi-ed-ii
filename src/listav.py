import sys
from search import bfs, dfs
from graph import AdjacencyListGraph, AdjacencyMatrixGraph

sys.dont_write_bytecode = True

"""
    Lista de Exercícios V:
    Grafos – Definições e Representações
"""

# Questão 9

graph_al = AdjacencyListGraph()

graph_al.addVertex('A')
graph_al.addVertex('B')
graph_al.addVertex('C')
graph_al.addEdge('A', 'B')
graph_al.addEdge('A', 'C')

print(graph_al.numberOfVertices())
print(graph_al.numberOfEdges())

# # Questão 10

grafo_am = AdjacencyMatrixGraph()

grafo_am.addVertex('A')
grafo_am.addVertex('B')
grafo_am.addVertex('C')
grafo_am.addEdge(0, 1)
grafo_am.addEdge(0, 2)

print(grafo_am.numberOfVertices())
print(grafo_am.numberOfEdges())
print(grafo_am.edges())