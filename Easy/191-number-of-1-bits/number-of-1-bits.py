class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        for i in range(32):
            res = n >> i & 1
            if res == 1:
                c += 1
        return c