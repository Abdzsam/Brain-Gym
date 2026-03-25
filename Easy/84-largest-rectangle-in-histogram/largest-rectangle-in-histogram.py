class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        mx = 0

        for i, height in enumerate(heights):
            start = i
            while stk and height < stk[-1][0]:
                h, j = stk.pop()
                w = i - j
                a = h * w
                mx = max(mx, a)
                start = j
            stk.append((height, start))

        for i in range(len(stk)):
            h, j = stk.pop()
            w = n - j
            mx = max(mx, h * w)

        return mx

            



        

        
        