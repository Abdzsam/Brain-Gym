class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = {}
        
        for i in range(len(nums)):
            if nums[i] in majority:
                majority[nums[i]] = majority[nums[i]] + 1
            else:
                majority[nums[i]] = 1

        for num, count in majority.items():
            if count > len(nums)/2:
                return num

            
