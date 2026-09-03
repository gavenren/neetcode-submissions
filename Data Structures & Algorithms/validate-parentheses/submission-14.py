class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"{" : "}", "(" : ")", "[" : "]"}
        stack = []

        for l in range(len(s)):
            if s[l] not in brackets and stack == []:
                return False
            elif s[l] in brackets:
                stack.append(s[l])
            elif brackets[stack[-1]] == s[l]:
                stack.pop()
            else:
                return False

        return len(stack) == 0