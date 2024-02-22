"""
Program creates a graph or network from a series of links.
Assumptions: Input is in a for of list with elements of the list being tuples.
            Single tuple represent link between two nodes. 
            Ex. ("A","B") this tuple represents two connected nodes A and B.
Output: Program returns dictionary with keys representing nodes and list of values represents connected nodes. 
"""
def id_nodes(pairs): # Function identify nodes from list of links
    plain_list = []
    for u,v in pairs: # Links unpacking
        plain_list.extend([u,v])
    nodes = set(plain_list) # Only unique value from list of all values 
    return nodes

def graph_create(nodes, pairs): # Function creates dictionary where key is a node and value represents list of connected nodes
    graph = {}
    for nd in nodes:
        graph[nd]=[]
        for elm1, elm2 in pairs:
            if elm1 == nd:
                graph[nd].append(elm2)
            elif elm2 == nd:
                graph[nd].append(elm1)
            else:
                pass
    return graph 

if  __name__ == "__main__":
    input = [("A",2), ("B",3),(5,4),(4,1), ("A","B"), ("A",4), ("B",1), (3,5)]
    nodes = id_nodes(input)
    graph =graph_create(nodes, input)
    print(graph)