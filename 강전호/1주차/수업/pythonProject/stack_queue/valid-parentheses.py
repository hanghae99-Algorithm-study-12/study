# s " []()"
def isValid(s):
    pair = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    stack=[]
    openner = "{[("
    for char in s:
        if (char in openner):
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if pair[char] != top:
                return False
    return not stack


assert isValid("{}()")
assert isValid("{[]}")
assert isValid("{[()]}")

assert not isValid("{}]")
assert not isValid("{{{{{{{{{{}}}}}}}}")

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


def isValid_l(s):
    pair = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    stack = Stack()
    openner = "{[("
    for char in s:
        if char in openner:
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            if stack.pop() != pair[char]:
                return False
    return stack.is_empty()



assert isValid_l("{[()]}")

assert not isValid_l("{}]")
assert not isValid_l("{{}")
assert isValid_l("{}()")
assert isValid_l("{[]}")
assert isValid_l("{[()]}")

assert not isValid_l("{}]")
assert not isValid_l("{{{{{{{{{{}}}}}}}}")
