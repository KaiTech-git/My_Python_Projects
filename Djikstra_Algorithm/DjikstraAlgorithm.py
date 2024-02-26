"""
Program looks for the shortest wy through the graph using Dijkstra's Algorithm.

Program is composed of two main elements:
- Graph class used to store graph in form of dictionary (attribute self.graph). 
    Dictionary representation of the graph was created by utilizing functions created in program
    GraphWithValues.py 
-  Graph class function dijkstra_distance which calculates shortest distance between selected node and every node
    a given graph. Function input: name of starting node, output: distance from every node to selected node in form of dictionary
    where key is node name and value represents shortest distance.
"""
import GraphWithValues
class Graph:
    def __init__(self, pairs):
        self.graph = GraphWithValues.graph_create(GraphWithValues.id_nodes(pairs), pairs) # Attribute representing graph
        self.nodes = self.graph.keys() # Attribute representing number of nodes in the graph.
    
    def dijkstar_distance(self, start_node):
        vis_nodes = {start_node} # Set with visited nodes
        fin_dist = {x:float('inf') for x in self.graph.keys()} # Distance from starting node initialized with infinity value for every node 
        fin_dist[start_node] = 0
        current_node= start_node
        not_visited = []
        while True: 
            for nb, dis in self.graph[current_node]: # Tuple unpacking where nb is neighbor of the current_node and dis is distance between them.
                
                if fin_dist[nb] > dis + fin_dist[current_node] : # statement evaluating wether current path is shorter than the one already evaluated.
                    fin_dist[nb] = dis + fin_dist[current_node]
                    
            # List with distances from neighbors of current_node to starting node. Based on this list algorithm decides which node to visit next.  
            dist_from_start = [(a, b + fin_dist[current_node]) for a,b in self.graph[current_node] ] 
            not_visited =[(a, b) for a, b in not_visited + dist_from_start if a not in vis_nodes]
            
            if len(vis_nodes) == len(self.nodes):
                break
            
            # Function calculating minimal distance from starting node to not visited nodes.
            # Function assigns next current_node.
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
    