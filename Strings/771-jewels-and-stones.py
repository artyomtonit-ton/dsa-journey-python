from typing import List

class Solution:
    def findCountJewels(self, jewels: str, stones: str) -> int:
        count_jewels = 0
        for i in stones:
            if i in jewels:
                count_jewels += 1

        return count_jewels
       

if __name__ == "__main__":
    s = Solution()
    print(s.findCountJewels("aA", "aAAbbbb"))