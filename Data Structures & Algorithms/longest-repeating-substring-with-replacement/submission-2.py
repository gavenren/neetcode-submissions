from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        max_len = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            window = r - l + 1
            most_repeats = max(count.values())
            if window - most_repeats > k:
                count[s[l]] -= 1
                l += 1
            else:
                max_len = max(max_len, window)
        return max_len