class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string

    def decode(self, s: str) -> List[str]:
        string_list = []
        passed = False
        reading = 0
        string = ""
        for i in range(len(s)):
            if passed is False:
                if s[i] == "#":
                    passed = True
                    if reading == 0:
                        string_list.append(string)
                        passed = False
                else:
                    reading = reading * 10 + int(s[i])
            else:
                string += s[i]
                reading -= 1
                if reading == 0:
                    string_list.append(string)
                    passed = False
                    string = ""

        return string_list