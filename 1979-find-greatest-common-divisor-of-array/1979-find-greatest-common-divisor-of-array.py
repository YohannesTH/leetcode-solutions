class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m = min(nums)
        M = max(nums)
        r = m
        gcd = 1
        while r > 0: 
            q, r = M // m, M % m
            if r != 0:
                M = m
                m = r
        if r == 0:
            gcd = m
        else:
            for i in range(1, r):
                if r % i == 0 and m % i == 0:
                    gcd = r
        return gcd 
