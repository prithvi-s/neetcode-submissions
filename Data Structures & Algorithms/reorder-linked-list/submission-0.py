# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp
        n = 0
        while head and prev: 
            temp1 = head.next
            temp2 = prev.next
            if n % 2 == 0:
                head.next = prev
                head = temp1
            else:
                prev.next = head
                prev = temp2
            n += 1
