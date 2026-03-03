class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        p1 = 0
        p2 = len(height) - 1
        
        while p2 > p1:
            if (p2 - p1) * (min(height[p2],height[p1])) > maxA:
                maxA = (p2 - p1) * (min(height[p2],height[p1]))
            
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
        return maxA

                
        