from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n <= 1:
            return 0
        graph = defaultdict(list)

        leaf = []
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        print(graph)
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaf.append(i)


        while n > 2:
            n -= len(leaf)
            new_leaf = []
            for i in leaf:
                adj = graph[i].pop()
                graph[adj].remove(i)

                if len(graph[adj]) == 1:
                    new_leaf.append(adj)
            leaf = new_leaf
        return leaf


sol = Solution()
print(sol.findMinHeightTrees(6,[[0,3],[1,3],[2,3],[4,3],[5,4]]))
