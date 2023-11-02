def dfs(grafo: dict, inicio: str, alvo: str):
    visitado, pilha = [], [inicio]
    caminho: list = []  # Cria lista para armazenar o caminho
    while pilha:
        vertice = pilha.pop()
        if vertice not in visitado:
            visitado.append(vertice)
            caminho.append(vertice)  # Adiciona o vértice ao caminho
            if vertice == alvo:
                return caminho
            pilha.extend(set(grafo[vertice]) - set(visitado)) 
    return []  # Se não encontra, retorna lista vazia
