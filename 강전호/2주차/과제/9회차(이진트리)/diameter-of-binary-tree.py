# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree(list, index):
    parent = None
    if (len(list) > index):
        value = list[index]

        if value is None:
            return
        parent = TreeNode(value)
        parent.left = make_tree(list, 2 * index + 1)
        parent.right = make_tree(list, 2 * index + 2)

    return parent


class Solution:
    result = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.result = max(self.result, left + right )
            return max(left, right) + 1

        dfs(root)
        return self.result


input = [1,2,3,4,5]
root = (make_tree(input, 0))
sol = Solution()
print(sol.diameterOfBinaryTree(root))
