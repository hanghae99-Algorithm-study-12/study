#정수 n을 1,2,3의 합으로 나타내는 방법


'''
2 -> 1 1 = 1
3 -> 1 1 1, 1 2 , 2 1  =3
4 -> 1 1 1 1 , 1 1 2, 1 2 1, 2 1 1, 2 2, 1 3, 3,1 = 7
5 -> 1 1 1 1 , 1 1 1 2, 1 1 2 1, 1 2 1 1, 2 1 1 1 , 1 1 3, 1 3 1, 3 1 1, 2 3 , 3 2
'''
def count(a):
    cnt=0
    def dfs(start,sum):
        nonlocal cnt
        start+=sum
        if start==a:
            cnt+=1
            return
        elif start>a:
            return

        for i in range(1,4):
            dfs(start,i)
    dfs(0,0)



    return cnt


T = int(input())
for i in range(T):
    a=int(input())
    print(count(a))
