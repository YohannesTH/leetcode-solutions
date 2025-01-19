class Solution:
    def finalString(self, s: str) -> str:
        if "i" not in s:
            return s
        temp, res = "", ""
        for char in s:
            if char != "i":
                temp += char
            else:
                for c in temp:
                    res = c + res
                temp = res
                res = ""
        return temp
