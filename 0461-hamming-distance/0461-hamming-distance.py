class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s, t = "", ""
        i, j = 0, 0
        
        while x >= 1:
            i = x % 2
            x = x // 2
            s = str(i) + s
        
        while y >= 1:
            j = y % 2
            y = y // 2
            t = str(j) + t

        if len(s) != len(t):
            if len(s) < len(t):
                diff = len(t) - len(s)
                while diff > 0:
                    s = "0" + s
                    diff -= 1
            else:
                diff = len(s) - len(t)
                while diff > 0:
                    t = "0" + t
                    diff -= 1
        
        count = 0
        for k in range(len(s)):
            if s[k] != t[k]:
                count += 1
        
        return count