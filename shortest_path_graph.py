import ipdb

def edge_to_graph(edges):
    if not edges:
        return {}
    graph = {}
    for edge in edges:
        if len(edge) == 2:
            sisi1 = graph.get(edge[0])
            sisi2 = graph.get(edge[1])
            if sisi1:
                sisi1.append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]
            if sisi2:
                sisi2.append(edge[0])
            else:
                graph[edge[1]] = [edge[0]]
    return graph


        

def shortest_path(edges, source, destination):
    graph = edge_to_graph(edges)
    if source == destination:
        return 0
    if destination in graph.get(source):
        return 1
    if not graph:
        return -1
    distance = 0
    queue = [[source, distance]]
    memo = {source}
    while len(queue) > 0:
        current = queue.pop(0)
        distance = current[1]
        current_node = current[0]
        if current_node == destination:
            return distance
        
        for branch in graph.get(current_node):
            if branch not in memo:
                memo.add(branch)
                queue.append([branch,distance+1])
    return -1

edges = [
    ['w','x'],
    ['x','y'],
    ['z','y'],
    ['z','v'],
    ['w','v']
]

print(shortest_path(edges,'w','z'))