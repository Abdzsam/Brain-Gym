class Solution:
    def scoreOfString(self, s: str) -> int:
        strLen = len(s) - 1
        score = 0
        for i in range(strLen):
            score += abs((ord(s[i]) - ord(s[i + 1])))
        return score
