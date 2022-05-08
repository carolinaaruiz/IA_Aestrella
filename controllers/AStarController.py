from models.Node import Node
from models.Edge import Edge
from views.Graph import Graph


class AStarController:
    open_nodes = []
    close_nodes = []
    short_path = []
    neighbors = []

    nodes = []

    current_node: Node = None
    start_node: Node = None
    end_node: Node = None

    def __init__(self):
        self.graph = Graph()
        # self.edge = Node()
        # self.node = Node()

    def __repr__(self):
        return str(self.__dict__)

    def main(self):
        print('In main of Controller')

    def get_node(self, name: str) -> Node:
        for node in self.nodes:
            if node.name == name:
                node_enc = node
        return node_enc

    def add_edge(self, start, end, cost, di=True):
        # arista para parte grafica
        self.graph.G.add_edge(start, end, weight=cost)
        # Si el grafo no es dirigido
        if not di:
            # Agrego otra arista en sentido contrario
            self.graph.G.add_edge(end, start, weight=cost)
        # parte logica
        # obtengo el nodo para guardar sus aristas
        node = self.get_node(start)
        node.edges.append(Edge(node, self.get_node(end), cost))

    def add_neighbors(self):
        current_neighbors = self.current_node.get_neighbors()
        for node in current_neighbors:
            if node not in self.close_nodes:
                self.neighbors.append(node)

            # is_close = False
            # for node_close in self.close_nodes:
            #     if node_close == node:
            #         is_close = True
            #         break
            # if not is_close:
            #     self.neighbors.append(node)

    def drawGraphs(self):
        self.graph.draw("TRABAJO PRACTICO FINAL IA 1")

# if __name__ == '__main__':
#     aStar = AStarController()
#     aStar.main()
