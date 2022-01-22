#모든 부분 집합을 리턴하라.
nums=[1,2,3]

def subset(nums):
    result=[]
    def dfs(index,path):
        result.append(path)
        for i in range(index,len(nums)):
            dfs(i+1,path+[nums[i]])
    dfs(0,[])
    return result
print(subset(nums))