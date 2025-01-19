class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            n = str(x)
            rev = ""
            for _ in n:
                rev = _ + rev
            if n == rev:
                return True
            else: 
                return False
        else:
            return False