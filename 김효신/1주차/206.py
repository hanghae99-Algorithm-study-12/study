# 반복구조
def reverseList(self, head: ListNode) -> ListNode:
    node = head # node = 1(->2->3->4->5->None)
    prev = None

    # node.next를 이전 prev 리스트로 계속 연결하면 뒤집어진 연결 리스트를 얻을 수 있다.

    while node: # 1일 때                               # 2일 때                ...... # 5일 때
        next = node.next # next = 2(->3->4->5->None) # next = 3(->4->5->None)        # next = None
        node.next = prev # node = 1 -> None          # node = 2 -> 1 -> None         # node = 5->4->3->2->1->None
        prev = node      # prev = node = 1 -> None   # prev = node = 2 -> 1 -> None  # prev = 5->4->3->2->1->None
        node = next      # node = 2(->3->4->5->None) # node = 3(->4->5->None)        # node = None

    return prev


# 재귀구조

def reverseList(self, head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)
