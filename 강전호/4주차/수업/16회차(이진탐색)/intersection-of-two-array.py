from bisect import bisect
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []

        if len(nums1) > len(nums2):
            nums2 = list(set(nums2))
            for i in nums2:
                if i in nums1:
                    answer.append(i)
        else:
            nums1 = list(set(nums1))
            for i in nums1:
                if i in nums2:
                    answer.append(i)
        return answer


def intersec_arrays(nums1, nums2):
    if not nums1 or not nums2:
        return []

    result = set()
    nums2.sort()
    for n1 in nums1:
        idx = bisect.bisect_left(nums2, n1)
        if len(nums2) > idx and n1 == nums2[idx]:
            result.add(n1)

    return list(result)
