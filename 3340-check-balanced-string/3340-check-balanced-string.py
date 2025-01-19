class Solution:
    def isBalanced(self, num: str) -> bool:
        s_odd, s_even = 0, 0
        for i in range(len(num)):
            if i % 2 == 0:
                s_even += int(num[i])
            else:
                s_odd += int(num[i])
        if s_odd == s_even:
            return True
        return False