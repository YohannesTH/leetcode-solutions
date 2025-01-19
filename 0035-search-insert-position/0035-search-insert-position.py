class Solution: 
    def searchInsert(self, nums: List[int], target: int) -> int: 
        n = len(nums) 
        l = 0 
        r = n-1 
        while l <= r: 
            mid = (l+r)//2 
            if nums[mid] == target: 
                return mid 
            elif nums[mid] > target: 
                r = mid - 1 
            else:  
                l = mid + 1 
        return l