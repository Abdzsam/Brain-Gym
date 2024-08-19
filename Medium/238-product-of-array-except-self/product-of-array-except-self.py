class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums.copy()
        prenum = prefix[0]
        prefix[0] = 1
        for i in range(1,len(nums)):
            prefix[i] = prenum
            prenum *= nums[i]

        suffix = nums.copy()
        sufnum = suffix[len(nums) - 1]
        suffix[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = sufnum
            sufnum *= nums[i]

        for i in range(len(nums)):
            nums[i] = prefix[i] * suffix[i]

        return nums

        
            
            
            

            
        