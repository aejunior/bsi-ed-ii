import sys
from search import bfs, dfs

sys.dont_write_bytecode = True

"""
    Lista de Exercícios VI:
    Algoritmos Elementares em Grafos
"""

# Questão 8

exemplo = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

print(" -> ".join(bfs(exemplo, 'A', 'F')))

# # Questão 9

print(" -> ".join(dfs(exemplo, 'A', 'B')))
