class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            return None
        topNode = self.top
        self.top = self.top.next
        return topNode.item

    def is_empty(self):
        return self.top is None


def test_node():
    assert Node(1, None).item == 1




def test_stack():
    '''
     스택은 3가지 기능을 요구
     1. push
     2. pop
     3. is_empty

     '''
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    assert stack.is_empty()



class Queue:
    def __init__(self):
        self.front = None

    def push(self, value):
        if not self.front:
            self.front = Node(value, None)
        else:
            node = self.front
            while node.next:
                node = node.next
            node.next = Node(value, None)

    def pop(self):
        if not self.front:
            return None

        node = self.front
        self.front = self.front.next # 앞의 부분에 그 다음 꺼를 이번에 준다

        return node.item

    def is_empty(self):
        return self.front is None

    def print_a(self):
        if not self.front:
            print("없어")
        else:
            node = self.front
            while node.next:
                print(node.item,end=" ")
                node = node.next
            print(node.item)
            print()

def test_queue():

    queue = Queue()

    queue.push(1)
    queue.print_a()
    queue.push(2)

    queue.push(3)
    queue.push(4)
    queue.push(5)


    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 5


    assert queue.pop() is None
    assert queue.is_empty()




test_node()
test_stack()
test_queue()
