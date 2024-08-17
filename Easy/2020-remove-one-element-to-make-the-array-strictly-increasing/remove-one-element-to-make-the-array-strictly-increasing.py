class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        numLen = len(nums)
        for i in range(numLen):

            newNums = nums.copy()
            del newNums[i]
            numLen = len(newNums)

            increasing = True
            for j in range(1,numLen):
                if(newNums[j] <= newNums[j-1]):
                    increasing = False
                    break
            if(increasing == True):
                return True
                                        
        
        return False
                
        