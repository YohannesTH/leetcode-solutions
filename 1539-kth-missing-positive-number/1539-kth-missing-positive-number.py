class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        n = 1
        while True:
            if n not in arr:
                count += 1
            if count == k:
                return n 
            n += 1
