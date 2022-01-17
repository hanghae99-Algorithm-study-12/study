# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print_all(self):
        while self:
            print(self.val, end=' ')
            self=self.next
        print()


def oddEvenList( head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next ,even.next = odd.next.next , even.next.next
        odd, even = odd.next,even.next
    odd.next = even_head

    return head




a5= ListNode(5)
a4= ListNode(4,a5)
a3= ListNode(3,a4)
a2= ListNode(2,a3)
a1= ListNode(1,a2)
oddEvenList(a1).print_all()