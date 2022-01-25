from collections import deque


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
def invert(root:TreeNode)->TreeNode:

    q = deque([root])

    while q:
        node=q.pop()
        if node:
            node.left,node.right=node.right,node.left

            q.append(node.left)
            q.append(node.right)

    return root
input=[4,2,7,1,3,6,9]                       #    4
print(invert(make_tree(input,0)))           #   2 7
                                            #1  3  6 9