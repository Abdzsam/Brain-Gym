class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lowMin = 0
        highMin = len(nums) - 1
        resMin = 0

        while lowMin <= highMin:
            mid = (lowMin + highMin) // 2

            if len(nums) == 2:
                if nums[0] < nums[1]:
                    resMin = 0
                    break
                else:
                    resMin = 1
                    break

            if len(nums) == 1:
                resMin = 0
                break

            if mid == len(nums) - 1:
                resMin = len(nums) - 1
                break

            if nums[mid] > nums[-1]:
                lowMin = mid + 1
            elif nums[mid] < nums[-1]:
                highMin = mid - 1

            resMin = lowMin

        sNum1 = nums[resMin:len(nums)]
        sNum2 = nums[0:resMin]
        sNumF = sNum1 + sNum2

        low = 0
        high = len(sNumF) - 1
        resF = 0

        while low <= high:
            mid = (low + high) // 2

            if sNumF[mid] == target:
                resF = mid
                break
            elif sNumF[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

            
        if sNumF[resF] != target:
            return -1

        if len(sNumF) == 1:
            return 0

        return (resMin + resF) % len(nums)
        

            
        
         

            
        