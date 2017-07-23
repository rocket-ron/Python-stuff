"""
Read a file that contains an adjacency matrix and construct a node-based graph.

The adjacency matrix file, adj.txt, contains the following:


0 0 0 1 1 0 1 0 1 0 1 0 0 0 0 1 1 0 1 0 1 1 0 1 1  
0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 1 1  
0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0  
1 1 0 0 0 1 0 0 1 1 0 1 0 0 0 1 0 0 0 0 1 1 0 1 1  
1 1 0 0 0 0 1 1 1 0 0 0 1 0 0 1 0 0 0 0 1 1 1 0 0  
0 0 0 1 0 0 1 0 1 0 0 1 0 0 0 0 0 0 0 1 0 0 0 1 0  
1 0 0 0 1 1 0 1 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 0 0  
0 0 1 0 1 0 1 0 1 0 0 1 1 1 0 1 0 0 1 0 0 0 0 1 0  
1 0 0 1 1 1 0 1 0 0 0 0 0 0 0 0 1 0 1 0 1 1 1 0 1  
0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 1 0  
1 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 1 1 1 0 0  
0 0 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0  
0 0 0 0 1 0 1 1 0 0 1 0 0 1 0 0 1 1 0 1 0 0 1 0 0  
0 0 0 0 0 0 0 1 0 0 1 0 1 0 1 0 1 0 0 1 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 0 0 1 0 0  
1 0 0 1 1 0 1 1 0 1 0 0 0 0 1 0 1 0 1 1 1 0 1 1 0  
1 0 0 0 0 0 0 0 1 1 0 0 1 1 0 1 0 0 0 0 0 1 0 1 0  
0 1 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 1 0 1 0 0 0  
1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 1 0 1 0 0 1 1 0 1 0  
0 0 0 0 0 1 0 0 0 0 0 1 1 1 0 1 0 1 0 0 1 0 1 1 0  
1 0 0 1 1 0 0 0 1 0 1 0 0 0 0 1 0 0 1 1 0 0 0 0 0  
1 0 0 1 1 0 0 0 1 0 1 0 0 0 0 0 1 1 1 0 0 0 0 1 1  
0 1 1 0 1 0 0 0 1 0 1 1 1 0 1 1 0 0 0 1 0 0 0 0 0  
1 1 0 1 0 1 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 1 0 0 0  
1 1 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0

"""


from graphnode import GraphNode 
from Queue import Queue

# breadth-first search algorithm
# graph is a dictionary of nodes such that name : node
# node is the name or value of the node


def bfs(graph, node):
    levels = {}

    d = []
    q = Queue()
    q.put((graph[node], 0))
    d.append(graph[node])

    while not q.empty():
        v, l = q.get()
        if l not in levels:
            levels[l] = []
        levels[l].append(v.value)
        for connection in v.get_connections():
            if connection not in d:
                q.put((connection, l+1))
                d.append(connection)
    return levels

# n1 and n2 are the node values or names
# g is the graph dictionary where n1 and n2 are part of the keys


def equidistant_nodes(g, n1, n2):
    l0 = bfs(g, n1)
    l1 = bfs(g, n2)

    eq = []
    for key in l0.keys():
        for node in l0[key]:
            if key in l1.keys():
                if node in l1[key]:
                    eq.append(node)
    eq.sort()
    return eq


def read_adj_file(fname):
    nodes = {}
    with open(fname) as f:
        row = 0
        for line in f:
            col = 0
            for bit in line.split():
                if bit == '1':
                    if col not in nodes.keys():
                        nodes[col] = GraphNode(col)
                    if row not in nodes.keys():
                        nodes[row] = GraphNode(row)
                    nodes[col].add_connections(nodes[row])
                col = col + 1
            row = row + 1
    return nodes


if __name__ == '__main__':
    graph_nodes = read_adj_file('adj.txt')

    print '0 and 1 : ' + str(len(equidistant_nodes(graph_nodes, 0, 1)))
    print '0 and 5 : ' + str(len(equidistant_nodes(graph_nodes, 0, 5)))
    print '1 and 8 : ' + str(len(equidistant_nodes(graph_nodes, 1, 8)))
