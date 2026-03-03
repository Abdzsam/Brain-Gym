class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        trap = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                trap += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                trap += rightMax - height[r]

        return trap


             
        