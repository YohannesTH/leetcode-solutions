class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        disC = []
        
        for i in range(num_people):
            disC.append(0)
        count = 1
        j = 1
        while candies > 0:
            if candies >= j:
                temp = count % num_people
                disC[temp - 1] += j
                candies -= j
                count += 1
                j += 1
            else: 
                disC[temp] += candies
                candies = 0
        return disC