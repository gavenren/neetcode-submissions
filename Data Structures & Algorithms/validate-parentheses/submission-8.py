class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"{" : "}", "(" : ")", "[" : "]"}
        left = []

        for l in range(len(s)):
            if s[l] not in brackets and left == []:
                return False
            elif s[l] in brackets:
                left.append(s[l])
            elif brackets[left[-1]] == s[l]:
                left.pop()
            else:
                return False

        if len(left) > 0:
            return False
        else:
            return True