from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergelist(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 and l2:
            if l1.val>l2.val:
                l1,l2=l2,l1
            l1.next =self.mergelist(l1.next,l2)
        return l1 or l2  # l1 에 값이 있다면 l1을 리턴 l1값이 None이라면 l2값을 리턴

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        half,slow,fast = None,head,head
        while fast and fast.next:
            half,slow,fast = slow,slow.next,fast.next.next
        half.next=None

        l1= self.sortList(head)
        l2 = self.sortList(slow)
        return self.mergelist(l1,l2)
