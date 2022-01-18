# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
     def print_all(self):
         while self:
             print(self.val, end=' ')
             self = self.next
         print()
from typing import Optional


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (not l1) or (l2 and l1.val > l2.val): # l1이 안비어 있거나 / (l2가 안비어있으면서 l1이 가르키는 게 l2가 가르키는 값보다 크고 )
            l1,l2 = l2,l1
        if l1:
            l1.next =self.mergeTwoLists(l1.next,l2)
        return l1


li_3=ListNode(4)
li_2=ListNode(2,li_3)
li_1=ListNode(1,li_2)

li2_3=ListNode(4)
li2_2=ListNode(3,li2_3)
li2_1=ListNode(1,li2_2)

li_1.print_all()
li2_1.print_all()

Solution().mergeTwoLists(li_1,li2_2).print_all()