class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums1 = nums1 + nums2
        nums2 = sorted(nums1)
        res = 0
        print(nums2)
        mid = float((len(nums2) + 1) / 2) - 1
        print(mid)
        
        if len(nums2) % 2 != 0:
            res = nums2[int(mid)]
        else:
            print(int(mid))
            print(math.ceil(mid))
            res = (nums2[int(mid)] + nums2[math.ceil(mid)]) / 2


        return res
        
        