class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        return sorted(t_list) == sorted(s_list)
        