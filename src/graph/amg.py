from .Graph import Graph
from .Vertex import Vertex
from .Edge import Edge



class AdjacencyMatrixGraph(Graph):
    def __init__(self):
        self.graph = {}
        self.num_vertices = 0
        self.matrix = []

    def numberOfVertices(self):
        return self.num_vertices

    def numberOfEdges(self):
        count = 0
        for row in self.matrix:
            count += sum(row)
        return count

    def addVertex(self, name: str = None, data: object = None):
        if name is None:
            name = self.num_vertices
        self.graph[name] = data
        self.num_vertices += 1
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * self.num_vertices)
        return Vertex(name, name, data)

    def vertexAt(self, i: int):
        vertices = list(self.graph.keys())
        if i < len(vertices):
            return Vertex(vertices[i], vertices[i], self.graph[vertices[i]])

    def addEdge(self, ui: int, vi: int, isDirected: bool = True, weight=None, data=None):
        if ui >= self.num_vertices or vi >= self.num_vertices:
            raise ValueError("Vértice não existe.")
        self.matrix[ui][vi] = 1
        if not isDirected:
            self.matrix[vi][ui] = 1
        return Edge(ui, vi, isDirected, weight, data)

    def edgeExists(self, ui: int, vi: int):
        if ui >= self.num_vertices or vi >= self.num_vertices:
            return False
        return self.matrix[ui][vi] == 1

    def vertices(self):
        return [Vertex(name, name, self.graph[name]) for name in self.graph.keys()]

    def edges(self):
        edges = []
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.matrix[i][j] == 1:
                    edges.append(Edge(i, j, True, None, None))
        return edges

    def outgoingEdgesFromVertex(self, ui: int):
        edges = []
        for i in range(self.num_vertices):
            if self.matrix[ui][i] == 1:
                edges.append(Edge(ui, i, True, None, None))
        return edges

    def adjacentVertices(self, ui: int):
        adjacent_vertices = []
        for i in range(self.num_vertices):
            if self.matrix[ui][i] == 1:
                adjacent_vertices.append(i)
        return adjacent_vertices