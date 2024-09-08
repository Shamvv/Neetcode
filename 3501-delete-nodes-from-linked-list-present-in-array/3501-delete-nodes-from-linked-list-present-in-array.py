# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy

        while current and current.next:
            if current.next.val in nums_set:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next