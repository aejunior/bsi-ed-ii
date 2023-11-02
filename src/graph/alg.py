from .Graph import Graph
from .Vertex import Vertex
from .Edge import Edge



class AdjacencyListGraph(Graph):
    def __init__(self):
        self.graph = {}
        self.num_vertices = 0

    def numberOfVertices(self):
        return self.num_vertices

    def numberOfEdges(self):
        count = 0
        for vertex in self.graph:
            count += len(self.graph[vertex])
        return count

    def addVertex(self, name: str = None, data: object = None):
        if name is None:
            name = self.num_vertices
        self.graph[name] = []
        self.num_vertices += 1
        return Vertex(name, name, data)

    def vertexAt(self, i: int):
        vertices = list(self.graph.keys())
        if i < len(vertices):
            return Vertex(vertices[i], vertices[i], self.graph[vertices[i]])

    def addEdge(self, ui: int, vi: int, isDirected: bool = True, weight=None, data=None):
        if ui not in self.graph:
            self.addVertex(ui)
        if vi not in self.graph:
            self.addVertex(vi)
        edge = Edge(ui, vi, isDirected, weight, data)
        self.graph[ui].append(edge)
        if not isDirected:
            reverse_edge = Edge(vi, ui, isDirected, weight, data)
            self.graph[vi].append(reverse_edge)
        return edge

    def edgeExists(self, ui: int, vi: int):
        if ui in self.graph:
            for edge in self.graph[ui]:
                if edge.target == vi:
                    return True
        return False

    def vertices(self):
        return [Vertex(name, name, self.graph[name]) for name in self.graph.keys()]

    def edges(self):
        all_edges = []
        for vertex in self.graph:
            for edge in self.graph[vertex]:
                all_edges.append(edge)
        return all_edges

    def outgoingEdgesFromVertex(self, ui: int):
        if ui in self.graph:
            return self.graph[ui]

    def adjacentVertices(self, ui: int):
        if ui in self.graph:
            adjacent_vertices = []
            for edge in self.graph[ui]:
                adjacent_vertices.append(edge.target)
            return adjacent_vertices