class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: 
            return False
        for char in word.lower():
            if char not in "0123456789abcdefghijklmnopqrstuvwxyz":
                return False
        vow_c, con_c = 0, 0
        for char in "aeiou":
            if char in word.lower():
                vow_c += 1
                break
        for char in "bcdfghjklmnpqrstvwxyz":
            if char in word.lower():
                con_c += 1
                break
        if vow_c == 0 or con_c == 0:
            return False
        return True


