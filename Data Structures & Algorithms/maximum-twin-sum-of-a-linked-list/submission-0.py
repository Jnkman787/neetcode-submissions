# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        rec = {}
        slow = head
        i = 0
        while slow:
            rec[i] = slow.val
            i += 1
            slow = slow.next
        
        ans = 0
        i, j = 0, len(rec) - 1
        while i <= j:
            ans = max(ans, rec[i] + rec[j])
            i += 1
            j -= 1
        return ans