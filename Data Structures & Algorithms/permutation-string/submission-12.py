class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        substring = {}
        for i in s1:
            substring[i] = 1 + substring.get(i, 0)
        
        for l in range(len(s2)):
            if s2[l] in substring:
                count = substring.copy()
                r = l
                while r < len(s2) and s2[r] in count:
                    if count[s2[r]] > 0:
                        count[s2[r]] -= 1
                        r += 1
                    else:
                        break
                    if max(count.values()) == 0:
                            return True

        return False
