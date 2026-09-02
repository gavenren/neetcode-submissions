from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        max_len = 0 
        most_repeats = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            most_repeats = max(most_repeats, count[s[r]])
            if r - l + 1 - most_repeats > k:
                count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len