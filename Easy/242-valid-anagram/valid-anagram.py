class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}

        for l in s:
            if(l in sMap):
                sMap[l] += 1
            else:
                sMap[l] = 1

        for l in t:
            if(l in sMap):
                sMap[l] -= 1
            else:
                return False

        for key in sMap:
            if(sMap[key] != 0):
                return False
        return True
        