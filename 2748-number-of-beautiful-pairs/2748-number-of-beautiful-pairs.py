class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count = 0
        def gcd(x, y):
            m = min(x, y)
            g = 1
            for i in range(2, m+1):
                if x % i == 0 and y % i == 0:
                    g = i
            return g

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                temp1 = int(str(nums[i])[0])
                temp = str(nums[j])
                l = len(temp)
                temp2 = int(temp[l-1])
                if gcd(temp1, temp2) == 1:
                    count += 1
        return count