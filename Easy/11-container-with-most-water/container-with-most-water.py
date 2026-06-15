class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1

        maxArea = 0

        while L < R:
            limit = min(height[L],height[R])
            area = limit * (R - L)

            maxArea = max(maxArea, area)

            if height[L] > height[R]:
                R = R - 1
            else:
                L = L + 1

        return maxArea
        

                
        