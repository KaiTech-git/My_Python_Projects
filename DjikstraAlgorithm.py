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
    
    def dijkstar_distance(self, start_node, end_node=0):
        vis_nodes = {start_node}
        fin_dist = {x:float('inf') for x in self.graph.keys()}
        fin_dist[start_node] = 0
        current_node= start_node
        not_visited = []
        while True: 
            for nb, dis in self.graph[current_node]:
                
                if fin_dist[nb] > dis + fin_dist[current_node] :
                    fin_dist[nb] = dis + fin_dist[current_node]
                    
            dist_from_start = [(a, b + fin_dist[current_node]) for a,b in self.graph[current_node] ]
            not_visited =[(a, b) for a, b in not_visited + dist_from_start if a not in vis_nodes]
            
            if len(vis_nodes) == len(self.nodes):
                break
            
            current_node, distance_un= min(not_visited,key=lambda x:x[1])

            vis_nodes.add(current_node)

        return fin_dist
                
    
    def __str__(self):
        graph_str = ""
        for nd in self.graph.keys():
            graph_str = graph_str +  str(nd) + " : " + str(self.graph[nd]) + "\n"
        return graph_str 
    
if __name__ == "__main__":
    input = [("Warszawa","Gdansk",426 ), ("Gdansk","Szczecin",313),("Warszawa","Wroclaw",328),
             ("Wroclaw","Szczecin",336), ("Szczecin","Koszalin", 148), ("Warszawa","Lodz",129), 
             ("Lodz","Krakow",209 ), ("Krakow","Rzeszow",160), ("Koszalin", "Gdynia", 176), ("Gdynia", "Gdansk", 10)]
    G = Graph(input)
    
    print(G.dijkstar_distance("Gdynia"))
    