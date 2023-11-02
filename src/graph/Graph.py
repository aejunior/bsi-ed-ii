from abc import ABC, abstractmethod




class Graph(ABC):
    @abstractmethod
    def numberOfVertices(self):
        """
            Retorna a quantidade de vértices do grafo
        """
        pass
    
    @abstractmethod
    def numberOfEdges(self):
        """
            Retorna a quantidade de arestas do grafo
        """
        pass
    
    @abstractmethod
    def addVertex(self, name:str=None, data:object=None):
        """
            Adiciona um novo vértice ao grafo e o retorna
        """
        pass

    @abstractmethod
    def vertexAt(self, i:int):
        """
            Retorna o vértice que está na posição i do grafo
        """
        pass

    @abstractmethod
    def addEdge(self, ui:int, vi:int, isDirected:bool=True, weight=None,
    data=None):
        """
            Adiciona uma aresta ao grafo e a retorna no final
        """
        pass

    @abstractmethod
    def edgeExists(self, ui: int, vi: int):
        """
            Retorna True se existe uma aresta (u, v) e False caso contrário
        """
        pass

    @abstractmethod
    def vertices(self):
        """
            Método gerador que retorna todos os vértices do grafo
        """
        pass

    @abstractmethod
    def edges(self):
        """
            Método gerador que retorna todos as arestas do grafo
        """
        pass

    @abstractmethod
    def outgoingEdgesFromVertex(self, ui: int):
        """
            Método gerador que retorna todas as arestas que incidem do vértice u
        """
        pass

    @abstractmethod
    def adjacentVertices(self, ui: int):
        """
            Método gerador que retorna todos os vértices adjacentes de u
        """
        pass
