# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value is None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

    return parent


def make_lst_by_bst(root, limit):
    if not root:
        return []

    lst = []
    q = deque([root])

    while q:
        if len(lst) > limit:
            break

        node = q.popleft()
        if node:
            lst.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            lst.append(None)

    return lst


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:
            nums = sorted(nums)

            n = len(nums) // 2
            sub1 = nums[0:n]
            sub2 = nums[n + 1:]
            node = TreeNode(nums[n])
            node.left = self.sortedArrayToBST(sub1)
            node.right = self.sortedArrayToBST(sub2)

            return node


sol = Solution()
print(make_lst_by_bst(sol.sortedArrayToBST([-10, -7, -3, -1, 0, 1, 4, 5, 7, 9]),12))
