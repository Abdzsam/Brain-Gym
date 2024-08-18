class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[f"{nums[i]}"] = nums[i]

        if(len(hashMap) < len(nums)):
            return True
        else:
            return False


        