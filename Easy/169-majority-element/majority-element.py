class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = {}
        
        for i in range(len(nums)):
            if nums[i] in majority:
                majority[nums[i]] = majority[nums[i]] + 1
            else:
                majority[nums[i]] = 1

            if majority[nums[i]] > len(nums)/2:
                return nums[i]

        

            
