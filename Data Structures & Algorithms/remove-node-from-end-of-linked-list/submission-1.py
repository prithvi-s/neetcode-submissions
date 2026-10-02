# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr  = head
        while curr:
            curr = curr.next
            l += 1
        if l <= 1:
            return None
        curr = head
        t = traverse_length = l - n
        if t == 0:
            return head.next
        for i in range(t - 1):
            curr = curr.next
        
        curr.next = curr.next.next

        return head