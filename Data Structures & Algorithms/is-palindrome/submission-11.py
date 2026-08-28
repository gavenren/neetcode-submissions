class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        str_list = list(lower_s)
        for char in str_list:
            if 48 > ord(char) or ord(char) > 57 and not 97 <= ord(char) <= 122:
                str_list[str_list.index(char)] = ""
        new_string = "".join(str_list)
        reversed_list = new_string[::-1]
        if reversed_list == new_string:
            return True
        return False