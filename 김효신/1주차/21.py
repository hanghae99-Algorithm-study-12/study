# 두 리스트는 정렬이 되어 있고,
# 그 리스트 두 개를 하나로 합쳐라
# 근데 정렬이 되어 있어
#
# 방법 1)
# 리스트 값 하나씩 비교하는 것 -> 시간 너무 오래 걸릴 듯
#
# 방법 2)
# 두개를 더해서 다시 정렬하는 것 -> 이것도 하나씩 비교해야 하니까 방법 1과 같은 시간이 필요한가?


# 재귀구조로 풀면, 방법 1의 리스트 값 하나씩 비교도 되고, 두번째 방법은 이건 아예 고려를 하지 않는다
# 근데 재귀구조의 장점은 추가 공간을 더 안 쓰기 때문에 공간 복잡도가 굉장히 낮다는 것!


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 반복구조로 푼 방법
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode])-> Optional[ListNode]:
        dummyNode = ListNode(0)
        runner = dummyNode
        while list1 or list2:
            if list1 is None:
                runner.next = list2
                list2 = list2.next
            elif list2 is None:
                runner.next = list1
                list1 = list1.next
            else:
                if list1.val < list2.val:
                    runner.next=list1
                    list1 = list1.next
                else:
                    runner.next = list2
                    list2 = list2.next
            runner = runner.next
        return dummyNode.next

# 재귀구조로 푼 방법

arr = [1, 2, 4]
arr2 = [1, 3, 4]

sol = Solution()
print(sol.mergeTwoLists(arr, arr2))