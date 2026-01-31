from typing import List

class Solution:
    def finddecibinary(self, n: str) -> int:
        max_n = 0
        
        for i in n:
            if int(i) > max_n:
                max_n = int(i)
                
        return max_n
       

if __name__ == "__main__":
    s = Solution()
    print(s.finddecibinary("32"))