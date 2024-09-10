# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = head

        while curr and curr.next:
            g = gcd(curr.val, curr.next.val)
            newnode = ListNode(g)

            newnode.next = curr.next
            curr.next = newnode
            curr = newnode.next
        
        return head