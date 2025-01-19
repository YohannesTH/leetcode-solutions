class Solution:
    def isHappy(self, n: int) -> bool:
        list = []
        while n != 1:
            sum = 0
            for i in str(n):
                sum += (int(i))**2
                n = sum
            if sum not in list:
                    list.append(sum)
            else:
                return False
        return True