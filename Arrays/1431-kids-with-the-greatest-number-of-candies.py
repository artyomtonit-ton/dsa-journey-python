from typing import List

class Solution:
    def findcountextracandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        list_bool = []
        
        for i in candies:
            if i + extraCandies >= maxCandies:
                list_bool.append(True)
            else:
                list_bool.append(False)
            
        return list_bool

       

if __name__ == "__main__":
    s = Solution()
    print(s.findcountextracandies([2, 3, 5, 1, 3], 3))