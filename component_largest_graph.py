def evaluate_largest_graph(graph, recent_node, memo=set()):
    if recent_node in memo:
        return 0 
    jumlah = 0
    if recent_node not in memo:
        memo.add(recent_node)
        for branch in graph[recent_node]:
            jumlah = jumlah + evaluate_largest_graph(graph, branch, memo)
        return jumlah+1 


def largest_component(graph):
    if not graph:
        return 0
    memo = set()
    max = 0
    for key, items in graph.items():
        value = evaluate_largest_graph(graph, key, memo)
        if value >= max:
            max = value
    return max

graph3 = {
0:[1,5,8],
1:[0],
2:[3,4],
3:[2,4],
4:[2,3],
5:[0,8],
8:[0,5]
}

print(largest_component(graph3))