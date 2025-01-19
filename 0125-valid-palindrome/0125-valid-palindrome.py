class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for char in s:
            if char not in "abcdefghijklmnopqrstuvwxyz0123456789":
                s = s.replace(char, "")
        rev = ""
        for char in s:
            rev = char + rev
        if rev == s:
            return True
        else:
            return False
