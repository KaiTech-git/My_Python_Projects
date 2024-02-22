import GraphWithValues
class Graph:
    def __init__(self, pairs):
        self.graph = GraphWithValues.graph_create(GraphWithValues.id_nodes(pairs), pairs)
        self.nodes = self.graph.keys()
    def naber_nodes(self, nodes):
        nb_list=[]
        for nd in nodes:
            nb_list.extend(self.graph[nd][0:-1])
        return nb_list 
    
    def dijkstar_distance(self, start_node, end_node):
        vis_nodes = {start_node}
        fin_dist = {x:None for x in self.graph.keys()}
        fin_dist[start_node] = 0
        current_node= start_node
        ## Add while loop to check for all
        for nb, dis in self.graph[current_node]:
            
            if fin_dist[nb] > dis + fin_dist[current_node] or fin_dist[nb] == None:
                fin_dist[nb] = dis + fin_dist[current_node]
        # Add option to define next node to investigate.
            
    
    def __str__(self):
        graph_str = ""
        for nd in self.graph.keys():
            graph_str =+  nd + " : " + str(graph[nd]) + "\n"
        return graph_str 
    
        