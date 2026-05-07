# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        nums = []

        curr = head
        lenL = 0

        while curr != None:
            nums.append(curr.val)
            curr = curr.next
            lenL += 1

        currE = head
        currE = currE.next
        count = 1

        while currE != None:
            currE.val = nums[-1 * count]
            currE = currE.next
            if currE == None:
                break
            currE.val = nums[count]
            currE = currE.next
            count += 1
            

