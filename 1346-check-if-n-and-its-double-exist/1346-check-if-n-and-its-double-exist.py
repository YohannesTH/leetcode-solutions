class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for num in arr:
            if num != 0:
                if num / 2 in arr:
                    return True
            else:
                arr.remove(num)
                if num in arr:
                    return True
        return False