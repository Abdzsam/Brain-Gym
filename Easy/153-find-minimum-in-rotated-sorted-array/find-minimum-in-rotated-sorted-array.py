class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        res = 0

        while low <= high:
            mid = (low + high) // 2

            if len(nums) == 2:
                if nums[0] < nums[1]:
                    return nums[0]
                else:
                    return nums[1]

            if len(nums) == 1:
                return nums[0]

            if mid == len(nums) - 1:
                return nums[low]

            if nums[mid] > nums[-1]:
                low = mid + 1
            elif nums[mid] < nums[-1]:
                high = mid - 1

            
        return nums[low]
                
            
            

    
        
            
        