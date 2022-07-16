
from typing import List

# With O(log n) time complexity
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1
        mid = 0

        while low <= high:
        
                mid = (high + low) // 2

                if nums[mid] < target:
                    low = mid + 1
        
                elif nums[mid] > target:
                    high = mid - 1
        
                else:
                    return mid
        
        return low

leet_code = Solution()


result_1 = leet_code.searchInsert([1,3,5,6], 5)
result_2 = leet_code.searchInsert([1,3,5,6], 2)
result_3 = leet_code.searchInsert([1,3,5,6], 7)
result_4 = leet_code.searchInsert([], 1)

print(result_1)
print(result_2)
print(result_3)
print(result_4)