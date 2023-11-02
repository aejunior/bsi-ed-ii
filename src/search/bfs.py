from collections import deque

def bfs(grafo: dict, fonte: str, alvo: str) -> list:
    pais: dict = {fonte: None}
    # Cria fila com o primeiro elemento
    fila: deque = deque([fonte])
    while fila:
        # Remove o primeiro elemento da fila
        vertice: str = fila.popleft()
        for vizinho in grafo[vertice]:
            vizinho: str
            if vizinho not in pais:
                # Se o vizinho não estiver no dicionário de pais
                # Adiciona o vizinho no dicionário de pais
                pais[vizinho] = vertice
                fila.append(vizinho)
                if vertice == alvo:
                    # Se o nó atual for o alvo, para a busca
                    # retorna o caminho
                    break

    caminho = [alvo]
    while pais[alvo] is not None:
        caminho.insert(0, pais[alvo])
        alvo = pais[alvo]

    return caminho

