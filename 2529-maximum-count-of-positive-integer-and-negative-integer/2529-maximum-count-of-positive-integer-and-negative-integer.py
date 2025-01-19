class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        z = nums.count(0)
        for num in nums:
            if num > 0:
                pos += 1
        return max(pos, len(nums) - pos - z)