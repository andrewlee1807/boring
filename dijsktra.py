import numpy as np
graph = {
    'a': {'b':3, 'c':4, 'd':7},
    'b': {'c':1, 'f':5},
    'c': {'f':6,'d':2},
    'd': {'e':3, 'g':6},
    'e': {'g':3, 'h':4},
    'f': {'e':1, 'h':8},
    'g': {'h':2},
    'h': {'g':2}
}

def dijkstra(graph, start, end):
    shortest_distance = {}
    track = {}
    unseenNodes = graph
    path = []
    max_distance = float('inf')
    # initialize
    for node in unseenNodes:
        shortest_distance[node] = max_distance
    shortest_distance[start] = 0

    while unseenNodes:
        min_distance_node = None
        for node in unseenNodes:
            if min_distance_node == None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node
        path_options = graph[min_distance_node].items()

        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track[child_node] = min_distance_node
        unseenNodes.pop(min_distance_node)

    currentNode = end
    print(shortest_distance[end])
    while currentNode != start:
        try:
            print(currentNode, " -> ", end="")
            currentNode = track[currentNode]
        except KeyError:
            print("No path is reachable")
            break

# dijkstra(graph, 'a', 'h')
arr = np.random.rand(10000)
print(type(arr))

import time
t1 = time.time()
ret = []
for i in arr:
    ret.append(str(i) in arr)
print("time", time.time() - t1)

t1 = time.time()
arr = set(arr)
ret = []
for i in arr:
    ret.append(str(i) in arr)
print("time", time.time() - t1)
print(type(arr))
