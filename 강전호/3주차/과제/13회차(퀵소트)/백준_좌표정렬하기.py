import sys
input = sys.stdin.readline

N = int(input())
arr=[]
for i in range(N):
    temp=[]
    a,b=map(int, input().split())
    arr.append([a,b])
arr.sort()
for i in range(len(arr)):
    print((arr)[i][0],(arr)[i][1])