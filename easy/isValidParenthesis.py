# ))(( -> false
# [(]) -> false
# ({}) -> true
# {[]} -> true
# ([)] -> false

# Example: {[]}
# stack = ["{"]
# stack = ["{", "]"]
# stack = ["{"]
# stack = [] -> true

# Example: ([)]
# stack = ["("]
# stack = ["(", "["]
# stack = ["(", "[", ] -> false (I'm expecting to close the "[")


# Time: O(n)
# Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:

        hash_table = {"(": ")", "[": "]", "{": "}"}
        open_par = {"(", "[", "{"}
        closed_par = {")", "]", "}"}
        stack = []

        for idx in range(0, len(s)):

            current_par = s[idx]

            if current_par in open_par:
                stack.append(current_par)

            if current_par in closed_par:

                if len(stack) == 0:
                    return False

                stack_top = stack[-1]
                if hash_table[stack_top] == s[idx]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

leet_code = Solution()
result_1 = leet_code.isValid("()")
result_2 = leet_code.isValid("()[]{}")
result_3 = leet_code.isValid("(]")
result_4 = leet_code.isValid("{[]}")
result_5 = leet_code.isValid("([)]")

print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)