from collections import defaultdict


def reconstruct(fromto):
    answer = []
    graph = defaultdict(list)
    for a, b in sorted(fromto):
        graph[a].append(b)
    print(graph)

    def dfs(start):
        while graph[start]:
            dfs(graph[start].pop(0))
        answer.append(start)

    dfs('JFK')
    return answer[::-1]

fromto = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
print(reconstruct(fromto))
