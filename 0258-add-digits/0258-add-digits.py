class Solution:
    def addDigits(self, num: int) -> int:
        if num < 0:
            num *= -1 
        n = str(num)
        while len(n) > 1:
            sum = 0
            for _ in n:
                sum += int(_)
            n = str(sum)
        return int(n)