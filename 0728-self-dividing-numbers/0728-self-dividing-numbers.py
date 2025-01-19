class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for n in range(left, right + 1):
            num = str(n)
            count = 0
            for char in num:
                if int(char) == 0 or n % int(char) != 0:
                    count += 1
            if count == 0:
                ans.append(n)
        return ans