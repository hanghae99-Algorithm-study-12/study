#전체수n을 입력받아 k개의 조합을 리턴.

def sol(n,k):
    result=[]
    def dfs(elements,start,k):
        if k==0:
            result.append(elements[:])
            return

        for i in range(start,n+1):
            elements.append(i)
            dfs(elements,i+1,k-1)  #[1],2,1
            elements.pop()


    dfs([],1,k)
    return result


print(sol(4,2))

