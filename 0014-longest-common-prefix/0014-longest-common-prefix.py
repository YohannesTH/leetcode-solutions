class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        j = 0
        str = strs[0]
        min = len(strs[0])
        for k in range(1, len(strs)):
            if len(strs[k]) < min:
                min = len(strs[k])
        for s in strs:
            if s == "":
                return common
        for char in str:
            for i in range(1, len(strs)):
                temp = strs[i]
                if char != temp[j]:
                    return common
            common += char
            
            if j < min - 1:
                j += 1
            else:
                return common
