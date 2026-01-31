from typing import List

class Solution:
    def findSmallerNumber(self, nums: List[int]) -> List[int]:
        smaller_nums = []
        
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            smaller_nums.append(count)
                    
        return smaller_nums

if __name__ == "__main__":
    s = Solution()
    print(s.findSmallerNumber([8, 1, 2, 2, 3]))