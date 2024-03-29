"""
Program creates a graph from a series of links.
Assumptions: Input is in a for of list with elements of the list being tuples.
            Single tuple represent link between two nodes and value describing the link
            Ex. ("Node1", "Node2", "Value") this tuple represents two connected nodes.
Output: Program returns dictionary with keys representing nodes and list of values represents connected nodes
and values of the connection. 
"""
def id_nodes(pairs): # Function identify nodes from list of links
    plain_list = []
    for u,v,value in pairs: # Tuple unpacking
        plain_list.extend([u,v])
    nodes = set(plain_list) # Only unique value from list of all values 
    return nodes

def graph_create(nodes, pairs, graph = {}): # Function creates dictionary where key is a node and value represents list of connected nodes with connection value.
    for nd in nodes:
        graph[nd]=[]
        for elm1, elm2, value in pairs:
            if elm1 == nd:
                graph[nd].append((elm2,value))
            elif elm2 == nd:
                graph[nd].append((elm1,value))
            else:
                pass
    return graph 
# Main body of the program returns graph in a form of dictionary.
if  __name__ == "__main__":
    input = [("Warszawa","Gdansk",426 ), ("Gdansk","Szczecin",313),("Warszawa","Wroclaw",328),
             ("Wroclaw","Szczecin","336"), ("Szczecin","Koszalin", 148), ("Warszawa","Lodz",129), 
             ("Lodz","Krakow",209 ), ("Krakow","Rzeszow",160)]
    nodes = id_nodes(input)
    graph =graph_create(nodes, input)
    for nd in graph.keys():
        print(nd + " : " + str(graph[nd]) )