class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        lowMin = 0
        highMin = n - 1

        while lowMin <= highMin:
            mid = (lowMin + highMin) // 2

            if nums[mid] > nums[-1]:
                lowMin = mid + 1
            else:
                highMin = mid - 1

        resMin = lowMin

        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            realMid = (mid + resMin) % n

            if nums[realMid] == target:
                return realMid
            elif nums[realMid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1