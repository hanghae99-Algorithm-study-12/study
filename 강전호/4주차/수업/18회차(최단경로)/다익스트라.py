INF = int(1e9)

def dijkstra_naive(graph, start):
    def get_smallest_node():
        min_value = INF
        idx = 0
        for i in range(1, N):
            if dist[i] < min_value and not visited[i]:
                min_value = dist[i]
                idx = i
        return idx

    N = len(graph)
    visited = [False] * N
    dist = [INF] * N

    visited[start] = True
    dist[start] = 0

    for adj, d in graph[start]:
        dist[adj] = d

    # N개의 노드 중 첫 노드는 이미 방문했으므로,
    # N-1번 수행하면 된다.
    for _ in range(N - 1):
        # 가장 가깝고 방문 안한 녀석을 고르고,
        cur = get_smallest_node()
        visited[cur] = True
        # 최단거리를 비교, 수정한다.
        for adj, d in graph[cur]:
            cost = dist[cur] + d
            if cost < dist[adj]:
                dist[adj] = cost

    return dist

import heapq

def dijkstra_pq(graph,start):
    N = len(graph)
    dist = [INF]*N

    q=[]
    # 방문 을 하면서 업데이트한다.
    heapq.heappush(q,(0,start))
    dist[start]=0
    #처음 방문 누적 비용은 0.

    while q:
        acc, cur = heapq.heappop(q)

        if dist[cur]<acc:
            continue

        for adj,d in graph[cur]:
            cost = acc+d
            if cost<dist[adj]:
                dist[adj]=cost
                heapq.heappush(q,(cost,adj))
    return dist