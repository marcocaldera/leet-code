
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0

        nums.sort()

        while index < len(nums) and nums[index] <= val:
            if nums[index] == val:
                nums.pop(index)
            else:
                index += 1

        return len(nums)

leet_code = Solution()


result_1 = leet_code.removeElement([], 1)
result_2 = leet_code.removeElement([1,2,3], 3)
result_3 = leet_code.removeElement([1,3,2,3], 2)
result_4 = leet_code.removeElement([1,1,2], 1)
result_5 = leet_code.removeElement([0,0,1,1,1,2,2,3,3,4], 2)

print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)