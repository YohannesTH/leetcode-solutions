class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        min1, min2 = nums1[0], nums2[0]
        max1, max2 = nums1[len(nums1) - 1], nums2[len(nums2) - 1]
        
        if min2 > max1 or min1 > max2:
            return -1
        
        if min1 > min2:
            for num in nums1:
                if num in nums2:
                    return num
        else:
            for num in nums2:
                if num in nums1:
                    return num
        return -1