# 0을 완료하기 위해서는 1을 끝내야한다는것을 [0,1]쌍으로 표현하는 n개의 코스가 있다.
# 모든 코스가 완료가능한가.
# 2,[[1,0]]
from collections import defaultdict


def canfinish(course,schedule):
    dic = defaultdict(list)
    for i in schedule:
        dic[i[0]].append(i[1])
    traced = set()
    def dfs(i):
        if i in traced:
            return False

        traced.add(i)
        for y in dic[i]:
            if not dfs(y):
                return False

        traced.remove(i)
        return True

    for x in list(dic):
        print(list(dic))
        if not dfs(x):
            return False
    return True


course=2
schedule=[[0,1]]
print(canfinish(course,schedule))