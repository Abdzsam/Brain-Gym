class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                return True
            hashMap[num] = num
        return False


        