class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def prime(num):
            if num == 1:
                return False
            for i in range(2, int((num)**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        a, b = 0, 0
        check = True
        max_distance = 0
        for i in range(len(nums)):
            if prime(nums[i]):
                if check:
                    a = i
                    check = False
                else:
                    b = i  
                if b != 0:
                    max_distance = max(max_distance, b - a)
        return max_distance     