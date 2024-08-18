class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashList = {}

        for s in strs:
            word = ''.join(sorted(s))
            if(word in hashList):
                hashList[word].append(s)
            else:
                hashList[word] = [s]


        return hashList.values()