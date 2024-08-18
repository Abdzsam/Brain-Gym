class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}

        for num in nums:
            if(num in numMap):
                numMap[num] += 1
            else:
                numMap[num] = 1

        sortedNumMap = sorted(numMap.items(), key = lambda item: item[1],reverse = True)

        Output = []
        for i in range(k):
            Output.append(sortedNumMap[i][0])

        return Output

        