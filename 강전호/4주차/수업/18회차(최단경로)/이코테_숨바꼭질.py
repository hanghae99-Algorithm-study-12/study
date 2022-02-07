import heapq
from collections import defaultdict
INF = int(1e9)

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def hide(graph):
    N = len(graph)
    dist = [INF for _ in range(N+1)]

    q=[]
    dist[0]=dist[1]=0
    heapq.heappush(q,(0,1))

    while q:
        acc, cur = heapq.heappop(q)

        if dist[cur]<acc:
            continue
        for adj in graph[cur]:
            cost=acc+1
            if cost<dist[adj]:
                dist[adj]=cost
                heapq.heappush(q,(cost,adj))
    max_dist = max(dist[1:])
    cnt = sum([1 for idx in range(1, N + 1) if dist[idx] == max_dist])

    return dist.index(max_dist), max_dist, cnt

print(hide(graph))
