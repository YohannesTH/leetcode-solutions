class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for digit in digits:
            num += str(digit)
        n = list(str(int(num) + 1))
        for i in range(len(n)):
            n[i] = int(n[i])
        return n