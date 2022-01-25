from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree(list,index):
    parent=None
    if(len(list)>index):
        value=list[index]

        if value is None:
            return
        parent = TreeNode(value)
        parent.left = make_tree(list, 2 * index + 1)
        parent.right = make_tree(list, 2 * index + 2)

    return parent



class Solution:
    result =0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0

            left= dfs(node.left)
            right=dfs(node.right)
            if node.left and node.val==node.left.val:
                left+=1
            else:
                left=0

            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result,right+left)
            return max(left,right)
        dfs(root)
        return self.result
input=[5,4,5,1,1,5]
root=(make_tree(input,0))
sol=Solution()
print(sol.longestUnivaluePath(root))



