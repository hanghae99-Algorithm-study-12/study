import collections
from typing import Deque


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 포인터 2개를 이용해 앞에서부터 체크
        # 한 포인터는 다른 포인터의 하나 뒤나 2개 뒤를 가리킨다
        # 회문의 최소조건이 인접합 문자와 같거나 하나 떨어진 문자와 같아야 하기 떄문
        # 포인터가 가리키는 인덱스를 ㅁ

        start_pointer = -1
        end_pointer = -1

        while start_pointer < len(s) - 1:
            if s[start_pointer] == s[end_pointer + 2]:




Solution().longestPalindrome("nnad")

