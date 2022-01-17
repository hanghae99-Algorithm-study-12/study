class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted(nums)

        for idx, num in enumerate(nums):
            print(idx)
            print(num)


Solution().arrayPairSum([1,4,3,2])