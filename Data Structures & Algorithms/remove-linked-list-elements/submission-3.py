# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        prev = head
        curr = head.next
        
        if head.next == None:
            if head.val == val:
                return None
            else:
                return head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = prev.next
        if head.val == val:
            head = head.next
        return head