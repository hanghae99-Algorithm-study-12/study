# 반복구조
def reverseList(head):
    prev = None

    while head:
        temp = head
        head = head.next
        temp.next = prev
        prev = temp

    return prev

# 재귀구조