from Graph1A import A, a_c, a_p
from Graph1B import B, b_c, b_p
from Graph1C import C, c_c, c_p

def low_node(cost, used):
    low = float("inf")
    lowest_node = None
    for node in cost:
        c = cost.get(node)
        if c < low and node not in used:
            low = c
            lowest_node = node
    return lowest_node

def dijkstra(graph, cost, parent):
    used = []
    node = low_node(cost, used)
    while node:
        c = cost[node]
        child = graph[node]
        for n in child.keys():
            new_cost = c + child[n]
            if cost[n] > new_cost:
                cost[n] = new_cost
                parent[n] = node
        used.append(node)
        node = low_node(cost, used)
    path = ['Finish']
    path_node = 'Finish'
    while path_node != 'Start':
        path.insert(0, parent[path_node])
        path_node = parent[path_node]
    return path
print("== Shortest Path for Graph A ==")
print(dijkstra(A, a_c, a_p))
print("== Shortest Path for Graph B ==")
print(dijkstra(B, b_c, b_p))
print("== Shortest Path for Graph C ==")
print(dijkstra(C, c_c, c_p))