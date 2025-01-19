class Solution:
    def romanToInt(self, s) -> int:
        thisDict = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C":100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
        num = 0
        check = False
        for i in range(len(s)):
            if check == True:
                check = False
                continue
            if i != len(s) - 1:
                temp = s[i] + s[i+1]
                if temp not in thisDict:
                    num += thisDict[s[i]]
                else:
                    num += thisDict[temp]
                    check = True
            else:
                    num += thisDict[s[i]]
        return num