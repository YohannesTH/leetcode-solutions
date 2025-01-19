class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False

        l, r = 1, num
        while l != r - 1:
            mid = (l + r) // 2
            if mid * mid > num:
                r = mid
            elif mid * mid < num:
                l = mid
            else:
                return True
        return False