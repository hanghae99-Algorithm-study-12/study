def permutate(num):
    result=[]
    prev=[]

    def dfs(elements):
        if len(elements)==0:
            result.append(prev[:])                  #resul=[[1,2,3]]

        for e in elements:
            next=elements[:] # next 1,2,3     2,3                   2

            next.remove(e)  # next 1,3        2                   []

            prev.append(e)  # prev 1           1,3                 1,3,2
            dfs(next)       # dfs([2,3])       dfs([2])             dfs([])
            prev.pop()      #
    dfs(num)
    return result

print(permutate([1,2,3]))