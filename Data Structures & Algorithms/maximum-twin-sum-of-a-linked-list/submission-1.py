# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None 
        while slow: 
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode 

        left, right = head, prev
        twinSum = 0
        while left and right:
            twinSum = max(twinSum, left.val + right.val)
            left = left.next
            right = right.next
        return twinSum