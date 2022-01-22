DFS 는 탐색하는 원소를 최대한 깊게 따라가야 합니다.
이를 구현하기 위해 인접한 노드 중 방문하지 않은 모든 노드들을 저장해두고,
가장 마지막에 넣은 노드를 꺼내서 탐색하면 됩니다. → 그래서 스택을 썼죠!

BFS는 현재 인접한 노드 먼저 방문해야합니다.
이걸 다시 말하면 인접한 노드 중 방문하지 않은 모든 노드들을 저장해두고, 
가장처음에 넣은 노드를 꺼내서 탐색하면 됩니다
`가정처음에 넣은 노드들..?` -> `큐`를 이용하면 BFS를 구현할수 있습니다.

```python
from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def bfs_queue(start):
    visited = [start]
    q = deque([start])

    while q:
        node = q.popleft()              
        for adj in graph[node]:         
            if adj not in visited:  
                q.append(adj)           
                visited.append(adj)     
                

    return visited


assert bfs_queue(1) == [1, 2, 3, 4, 5, 6, 7]
```