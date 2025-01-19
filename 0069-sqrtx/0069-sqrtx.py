class Solution:
    def mySqrt(self, x: int) -> int:
        count = 0
        if x == 1:
            return x
        else:
            for i in range(x+1):
                if i*i == x:
                    return i
                elif i*i > x:
                    count += 1
                    return i-1
                    