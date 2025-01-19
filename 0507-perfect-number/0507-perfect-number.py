class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        import math
        if num <= 0:
            return False
        if num == 1:
            return False
        sum = 1
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                sum = sum + i
                sum += (num // i)
        if num == sum:
            return True
        return False 