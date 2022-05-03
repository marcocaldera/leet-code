from typing import List

# Time: O(m*n)
# Space: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)

        result = ""
        initial_word = strs[0]


        for index in range(len(initial_word)): # O(m)
            for word in strs[1:]: # O(n-1)
                if initial_word[index] != word[index]:
                    return result
            result += initial_word[index]
        
        return result


leet_Code = Solution()
result_1 = leet_Code.longestCommonPrefix(["flower","flow","flight"])
result_2 = leet_Code.longestCommonPrefix(["dog","racecar","car"])

print(result_1)
print(result_2)