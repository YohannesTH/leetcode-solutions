class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = len(nums)
        while val in nums:
            nums.remove(val)
            count -= 1
        return count