# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
    def print_all(self):
        while self:
            print(self.val, end=' ')
            self= self.next
        print()

def reverseList(head): #재귀
    def reverse(node,prev:ListNode= None):
        if not node:
            return prev
        next, node.next = node.next,prev
        return reverse(next,node)
    return reverse(head)

def reverseListr(head): #반복
    node, prev = head, None

    while node:
        next, node.next = node.next, prev  # 현재 노드에서 가르키는 노드를 next에, 현재 노드가 가르키고 있던것을 prev로
        prev, node = node, next            # prev를 현재 노드로 최신화, node도 현재 노드에서 가르키고 있는 노드로 최신화
    return prev

li_5=ListNode(5)
li_4=ListNode(4,li_5)
li_3=ListNode(3,li_4)
li_2=ListNode(2,li_3)
li_1=ListNode(1,li_2)


li_1.print_all()
reverseListr((li_1)).print_all()
