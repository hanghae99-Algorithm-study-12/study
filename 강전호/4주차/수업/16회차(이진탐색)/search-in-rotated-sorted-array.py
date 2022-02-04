# class Solution:
#     def search(self, nums, target):
#         # [4, 5, 6, 7, 0, 1, 2] -> [0,1,2,4,5,6,7]
#         #  targer 7 -> 3
#         # target 1-> 1  5-4
#         max = 0
#         for i in range(0, len(nums)):
#             if nums[i] > nums[max]:
#                 max = i
#
#         def bs1(start, end):
#             mid = max
#             print(max)
#             if target > nums[mid]:
#                 print("s")
#                 return -1
#
#             if nums[0] == target:
#                 return 0
#             elif target == nums[mid]:
#                 return mid
#             elif nums[end] == target:
#                 return end
#             elif nums[0] < target:
#                 return bs(0, mid - 1)
#             elif target < nums[end]:
#                 return bs(mid + 1, end)
#             else:
#                 return -1
#
#         def bs(start, end):
#             if start > end:
#                 return -1
#
#             mid = (start + end) // 2
#
#             if nums[mid] < target:
#                 return bs(mid + 1, end)
#             elif nums[mid] > target:
#                 return bs(start, mid - 1)
#             else:
#                 return mid
#
#         return bs1(0, len(nums) - 1)
def bs_rotated(nums, target):
    def bs(lst, start, end):
        if start > end:
            return -1

        mid = (start + end) // 2
        if lst[mid] < target:
            return bs(lst, mid + 1, end)
        elif lst[mid] > target:
            return bs(lst, start, mid - 1)
        else:
            return mid

    if not nums:
        return -1

    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    added = nums + nums[:left]

    result = bs(added, left, len(added) - 1)
    return result if result == -1 else result % len(nums)