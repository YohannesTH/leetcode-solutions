class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        count = 0
    
        for num in range(l, r+1):
            c = 0
            for i in range(1, num):
                if num % i == 0: 
                    c += 1
                if c > 2:
                    break
            if c == 2:
                count += 1        
        return r + 1 - l - count 