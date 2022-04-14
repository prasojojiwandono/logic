def evaluate_graph(current, graph, memo=set({})):
    if current in memo:
        return False, memo
    memo.add(current)
    for isi in graph.get(current):
        evaluate_graph(isi, graph, memo)
    return True, memo


def component_count_graph(graph):
    if len(graph) == 0:
        return 0
    memo = set({})
    count = 0 
    for key, items in graph.items():
        value, memo = evaluate_graph(key, graph, memo)
        if value:
            count = count + 1
    return count

graph = {
    0: [8,1,5],
    1: [0],
    5: [0,8],
    8: [0,5],
    2: [3,4],
    3: [2,4],
    4: [3,2],
}
graph2 = {
    1:[2],
    2:[1],
    3:[],
    4:[6],
    5:[6],
    6:[4,5,7,8],
    7:[6],
    8:[6]
}

graph3 = {
    0:[1,5,8],
    1:[0],
    2:[3,4],
    3:[2,4],
    4:[2,3],
    5:[0,8],
    8:[0,5]
}

print(component_count_graph(graph2))
