class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec = set()

        for i in range(len(nums)):
            consec.add(nums[i])

        nums = sorted(consec)
        print(nums)
        count = 0
        intcount = 1

        if len(nums) == 1:
            return 1

        for i in range(len(nums)):
            if(i == len(nums) - 1):
                intcount += 1
                break
            j = i + 1
            if(abs(nums[j] - nums[i]) == 1):
                intcount += 1
            else:
                intcount = 1
            print(str(intcount) + "with" + str(nums[j]))

            count = max(intcount, count)

        return count
        