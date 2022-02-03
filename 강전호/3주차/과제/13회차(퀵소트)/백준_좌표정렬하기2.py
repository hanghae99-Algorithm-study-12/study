import sys
input = sys.stdin.readline

N = int(input())
arr=[]
for i in range(N):
    temp=[]
    a,b=map(int, input().split())
    arr.append([a,b])
arr.sort(key=lambda x:(x[1],x[0]))
#arr.sort()

for i in range(len(arr)):
    print((arr)[i][0],(arr)[i][1])

# 걍 반대로 a랑 b를 반대로 저장해서 출력을 반대로 해주면 전에 푼 문제랑 똑같다