
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1

        while index < len(nums):
            if nums[index - 1] == nums[index]:
                nums.pop(index)
            else:
                index += 1

        print(nums)
        return len(nums)

leet_code = Solution()


result_1 = leet_code.removeDuplicates([]) # [] return 0
result_2 = leet_code.removeDuplicates([1,2,3]) # [1,2,3] return 3
result_3 = leet_code.removeDuplicates([1,2,3,3]) # [1,2,3] return 3
result_4 = leet_code.removeDuplicates([1,1,2]) # [1,2] return 2
result_5 = leet_code.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) # [0,1,2,3,4] return 5

print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)