class Solution:
    def isThree(self, n: int) -> bool:
        if n < 0:
            n = n * (-1)
        count = 0    
        for i in range(2, n):
            if n % i == 0:
                count += 1
        if count == 1:
            return True
        return False