class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for string in strs:
            anagram = [0] * 26
            for char in string:
                anagram[ord(char) - 97] += 1
            anagram = tuple(anagram)
            if anagram not in res:
                new_list = [string]
                res[anagram] = new_list
            else:
                res[anagram].append(string)
        result = list(res.values())
        return result
            
            
