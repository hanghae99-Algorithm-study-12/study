n = int(input())
arr = list(map(int, input().split()))
k = int(input())
#리프노드는 자식의 개수가 0개인것.
#k가 인덱스

# 돌아가면서 삭제
def dfs(arr,k):
    arr[k]=-10
    for i in range(len(arr)):
        if arr[i] == k:
            dfs(arr,i)

ans=0
dfs(arr,k)
for i in range(len(arr)):
    if i not in arr and arr[i] != -10:
        ans+=1
print(arr)
print(ans)