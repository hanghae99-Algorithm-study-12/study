def dfs_recursive(node, visited,graph):
    # 방문처리
    visited.append(node)

    # 인접 노드 방문
    for adj in graph[node]:
        if adj not in visited:
            dfs_recursive(adj, visited,a)

    return len(visited)-1
def dfs_stack(start,graph):
    visited = []
    # 방문할 순서를 담아두는 용도
    stack = [start]

    # 방문할 노드가 남아있는 한 아래 로직을 반복한다.
    while stack:
        # 제일 최근에 삽입된 노드를 꺼내고 방문처리한다.
        top = stack.pop()

        if top not in visited:
            visited.append(top)
        # 인접 노드를 방문한다.
        for adj in graph[top]:
            if adj not in visited:
                stack.append(adj)

    return len(visited)-1
a={}

n=int(input())
for i in range(1,n+1):
    a[i]=[]
m=int(input())
for i in range(m):
    x,y=map(int,input().split())
    a[x].append(y)
    a[y].append(x)


print((dfs_recursive(1,[],a)))
