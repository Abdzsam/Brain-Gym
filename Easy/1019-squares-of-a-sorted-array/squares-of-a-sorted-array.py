class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        minNum = nums[-1]
        minCo = 0
        for i in range(len(nums)):
            if abs(nums[i]) < abs(nums[minCo]):
                minCo = i
        
        minNum = nums[minCo]
        l = minCo - 1
        r = minCo + 1
        result = []
        result.append(minNum**2)

        while l >= 0 or r < len(nums):

            if l < 0:
                result.append(nums[r]**2)
                r += 1
                continue

            if r >= len(nums):
                result.append(nums[l]**2)
                l -= 1
                continue

            if nums[l]**2 < nums[r]**2:
                result.append(nums[l]**2)
                l -= 1
            else:
                result.append(nums[r]**2)
                r += 1

        return result