class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        l, count = len(nums), 0
        for i in range(l):
            for j in range(i+1, l):
                if nums[i] + nums[j] < target:
                    count += 1
        return count
        