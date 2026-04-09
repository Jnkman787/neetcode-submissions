# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        reverse = ListNode(head.val)
        while head.next != None:
            temp = reverse
            head = head.next
            reverse = ListNode(head.val, next=temp)

        return reverse