class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        m = min(limit, n)
        for i in range(m+1):
            for j in range(m+1):
                for k in range(m+1):
                    if i + j + k == n:
                        count += 1
        return count