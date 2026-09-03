class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""

        t_count = {}

        for char in t:
            t_count[char] = 1 + t_count.get(char, 0)

        s_count = {}
        matches = 0
        goal = len(t_count)

        left = 0
        best_start = 0
        best_length = float("inf")

        for right in range(len(s)):
            char = s[right]

            if char in t_count:
                s_count[char] = 1 + s_count.get(char, 0)

                if s_count[char] == t_count[char]:
                    matches += 1

            # Shrink the window while it remains valid
            while matches == goal:
                current_length = right - left + 1

                if current_length < best_length:
                    best_length = current_length
                    best_start = left

                left_char = s[left]

                if left_char in t_count:
                    s_count[left_char] -= 1

                    if s_count[left_char] < t_count[left_char]:
                        matches -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_start : best_start + best_length]