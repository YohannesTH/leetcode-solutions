class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def co_prime(i, j):
            m = min(i, j)
            for x in range(2, m+1):
                if i % x == 0 and j % x == 0:
                    return False
            return True

        simp_frac = []
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if (i / j) != 1 and co_prime(i, j):
                    simp_frac.append(str(i) + "/" + str(j))
        return simp_frac