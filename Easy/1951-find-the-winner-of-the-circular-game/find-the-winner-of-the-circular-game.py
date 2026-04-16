class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        frnds = []
        for i in range(n):
            frnds.append(i+1)

        i = 0

        while len(frnds) > 1:
            i = (i + k - 1) % len(frnds)
            del frnds[i]

        return frnds[0]