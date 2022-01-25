from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
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


def test_max_depth(lst):
    root = make_tree_by(lst, 0)

    if not root:
        return 0

    q = deque([root])

    depth = 0

    while q:
        depth += 1
        for _ in range(len(q)):
            cur = q.popleft()
            print(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    return depth


#print(test_max_depth(lst=[]))
print(test_max_depth(lst=[4,2,7,1,3,6,9]))
