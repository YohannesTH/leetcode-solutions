class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        thisdict = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8} 
        diff1 = thisdict[coordinate1[0]] - thisdict[coordinate2[0]]
        diff2 = int(coordinate1[1]) - int(coordinate2[1])
        diff = diff1 + diff2
        if diff % 2 == 0:
            return True
        return False