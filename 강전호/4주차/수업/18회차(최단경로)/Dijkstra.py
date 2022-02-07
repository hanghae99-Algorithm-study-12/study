import sys

from 다익스트라 import dijkstra_naive

with open('testcase1.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline
    n, m = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

print(graph)
assert dijkstra_naive(graph, start) == [1000000000, 0, 2, 3, 1, 2, 4]
