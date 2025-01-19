class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        while i * (i+1) / 2 <= n:
            i += 1
        return i - 1 