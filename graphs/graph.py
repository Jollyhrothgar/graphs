import copy



class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            self.graph_dict = {}
        else:
            self.graph_dict = copy.deepcopy(graph_dict)

    def add_node(self, node_id, data=None, connections=[]):
        if node not in self.graph_dict:
            self.graph_dict


print(hash(lambda x: x - 1))
print(hash(lambda x: x - 1))

g1 = Graph()
g2 = Graph()


print(hash(g1))
print(hash(g2))
print(hash(-1))
 
val = -1
print(hash(val))

