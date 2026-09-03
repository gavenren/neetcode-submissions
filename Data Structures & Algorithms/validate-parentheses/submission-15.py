class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"{" : "}", "(" : ")", "[" : "]"}
        stack = []

        for l in range(len(s)):
            if s[l] not in brackets:
                if stack == []:
                    return False
                elif brackets[stack[-1]] == s[l]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[l])
            


        return len(stack) == 0