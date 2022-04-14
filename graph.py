graph = {
    'a':['c','b'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}

# deep first graph (dfg)
def dfg(graph, root):
    if not graph.get(root):
        return [root]
    res = [root] 
    for branch in graph[root]:
        res = res + dfg(graph,branch)
    return res

# breadth first graph (bfg)
def bfg(graph, root):
    queue = []
    urutan = []
    queue.append(root)
    while len(queue)>0:
        current = queue.pop(0)
        urutan.append(current)

        isi = graph.get(current)
        if isi:
            for part_isi in isi:
                queue.append(part_isi)
    return urutan


graph2 = {
    'f':['g','i'],
    'g':['h'],
    'h':[],
    'i':['g','k'],
    'j':['i'],
    'k':[]
}            

def has_path(graph, source, destination):
    if source == destination:
        return True
    elif not graph[source]:
        return False
    
    isi = graph.get(source)
    for component_isi in isi:
        if has_path(graph, component_isi, destination) == True:
            return True
    return False


edges = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n']
]

def edges_to_graph(edges):
    graph = {}
    for edge in edges:
        if len(edge) == 2:
            isi0 = graph.get(edge[0])
            isi1 = graph.get(edge[1])
            if isi0:
                isi0.append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]
            
            if isi1:
                isi1.append(edge[0])
            else:
                graph[edge[1]] = [edge[0]]
    return graph

def has_path_undirect(graph, node1, node2, memo={}):
    if node1 == node2:
        return True
    elif not graph.get(node1):
        return False
    branches = graph.get(node1)
    for branch in branches:
        if branch not in memo:
            memo = list(memo)
            memo.append(branch)
            memo = set(memo)
            if has_path_undirect(graph, branch, node2, memo):
                return True
            
    return False

def has_path_undirect_edges(edges, node1, node2):
    graph = edges_to_graph(edges)
    result = has_path_undirect(graph, node1, node2)
    return result

print(dfg(graph,'a'))
print(bfg(graph,'a'))
print(has_path(graph2,'f','k'))
print(edges_to_graph(edges))
print(has_path_undirect_edges(edges, 'k','o'))