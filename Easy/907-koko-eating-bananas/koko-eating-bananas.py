class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        sortedP = sorted(piles)

        low = 1
        high = sortedP[-1]
        while low <= high:
            mid = (low + high) // 2

            tt = 0
            for pile in piles:
                tt += math.ceil(pile / mid)

            if tt <= h:
                high = mid - 1
            elif tt > h:
                low = mid + 1

            
        return low
            
