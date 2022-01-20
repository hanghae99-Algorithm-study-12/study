from collections import defaultdict


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 100
        self.table = defaultdict(ListNode)

    def put(self, key: int, value: int):
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int):
        index = key % self.size

        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self,key:int):
        index = key % self.size
        if self.table[index].value is None:
            return
        p = self.table[index]

        if p.key == key:        #인덱스의 처음 노드 일 경우 삭제하는 경우
            self.table[index] =ListNode() if p.next is None else p.next
            return

        prev = p
        while p:
            if p.key==key:
                prev.next = p.next  # 연결을 끊어주기
                return
            prev,p = p,p.next
