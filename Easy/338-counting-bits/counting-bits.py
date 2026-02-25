class Solution:
    def countBits(self, n: int) -> List[int]:
        b = []
        for i in range(n + 1):
            c = 0
            for j in range(32):
                if i >> j & 1:
                    c += 1

            b.append(c)

        return b