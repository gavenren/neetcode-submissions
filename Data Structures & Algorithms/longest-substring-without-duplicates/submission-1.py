class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        longest_length = 0
        characters = []
        r = 0
        while r < len(s):
            if s[r] in characters:
                characters.append(s[r])
                characters = characters[characters.index(s[r]) + 1:]
            else:
                characters.append(s[r])
            longest_length = max(longest_length, len(characters))

            r += 1

        return longest_length