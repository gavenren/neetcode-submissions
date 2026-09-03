class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"{" : "}", "(" : ")", "[" : "]"}
        stack = []

        for l in s:
            if l not in brackets:
                if stack and brackets[stack[-1]] == l:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)
            


        return len(stack) == 0