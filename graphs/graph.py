import copy



class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            self.graph_dict = {}
        else:
            self.graph_dict = copy.deepcopy(graph_dict)

    def add_node(self, node, attrs):
        if node not in self.graph_dict:
            self.graph_dict


