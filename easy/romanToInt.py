# Time: O(n)
# Space: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        hash_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        result = 0

        for idx, elem in enumerate(s):

            result += hash_table[elem]

            if idx != 0:
                previous_elem = s[idx - 1]
                combined = previous_elem + elem

                if combined in hash_table:
                    result -= hash_table[previous_elem] # because I added it on the previous iteration
                    result -= hash_table[elem] # because I just added it
                    result += hash_table[combined]
    
        return result


leet_Code = Solution()
result_1 = leet_Code.romanToInt("III")
result_2 = leet_Code.romanToInt("LVIII")
result_3 = leet_Code.romanToInt("MCMXCIV")

print(result_1)
print(result_2)
print(result_3)