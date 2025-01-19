class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        largest_prime = 0
        def prime(num):
            if num == 1:
                return False
            for i in range(2, int((num)**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        for i in range(len(nums)):
            if prime(nums[i][i]):
                largest_prime = max(largest_prime, nums[i][i])
            if prime(nums[i][len(nums) - i - 1]):
                largest_prime = max(largest_prime, nums[i][len(nums) - i - 1]) 
        return largest_prime