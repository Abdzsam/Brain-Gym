class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec = set(nums)
        longest = 0

        for num in consec:
            if (num - 1) not in consec:
                length = 1
                while (num + length) in consec:
                    length += 1
                longest = max(length, longest)
        return longest