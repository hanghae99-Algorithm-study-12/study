# 36ms , 19.3MB

import collections
from typing import Deque


class Solution:
    def is_palindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop() != strs.popleft():
                return False
        return True