from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        print("s")
        #[2,7,5,11,15] 9  -> [1,2]
        #[2,3,4] 6 ->[1 3]
        left = 0
        right = len(numbers)-1
        print("sss")
        while True:
            print("S",left,right)
            if numbers[left]+numbers[right]<target:
                print("l")
                left+=1
            elif numbers[left] + numbers[right] > target:
                print("r")
                right-=1
            else:

                return [left+1,right+1]
s=Solution()
print(s.twoSum([2,7,5,11,15], 9))