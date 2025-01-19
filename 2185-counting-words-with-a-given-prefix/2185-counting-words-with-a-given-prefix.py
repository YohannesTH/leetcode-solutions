class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count, check = 0, 0
        for word in words:
            check = 0
            for i in range(len(pref)):
                if check != 0:
                    continue
                if i < len(word):
                    if pref[i] != word[i]:
                        check += 1
                else:
                    check += 1
            if check == 0:
                count += 1
        return count