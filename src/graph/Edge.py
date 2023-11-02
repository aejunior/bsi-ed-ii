class Edge:
    def __init__(self, source, target, is_directed=True, weight=None, data=None):
        self.source = source
        self.target = target
        self.is_directed = is_directed
        self.weight = weight
        self.data = data
