class Solution:
    def reverseBits(self, n: int) -> int:
        revNum = 0
        for i in range(32):
            revNum = revNum << 1
            revNum = revNum | (n >> i & 1)
            print(revNum)
            

        return revNum
        