class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        p1 = nums[0] * nums[1] * nums[l-1]
        p2 = nums[l-1] * nums[l-2] * nums[l-3]
        return max(p1, p2)