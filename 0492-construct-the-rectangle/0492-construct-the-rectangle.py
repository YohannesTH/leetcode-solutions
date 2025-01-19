class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        diff = area
        opt = [0, 0]
        for w in range(1, int((area ** 0.5)) + 1):
            if area % w == 0:
                l = int(area / w)
                if l - w < diff:
                    diff = l - w
                    opt = [l, w]
        return opt