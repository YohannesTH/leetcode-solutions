class Solution:
    def findComplement(self, num: int) -> int:
        s = ""
        i = 0
        while num >= 1:
            i = num % 2
            num = num // 2
            s = str(i) + s
        
        rev = ""
        for _ in s:
            if _ == "0":
                rev += "1"
            else:
                rev += "0"
        
        comp = 0
        c = len(rev) - 1
        for char in rev:
            comp += ((2**c) * int(char)) 
            c -= 1
        
        return comp