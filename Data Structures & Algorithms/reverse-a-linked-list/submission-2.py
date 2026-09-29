# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next
        if stack:
            headn = stack.pop()
            curr=headn
        else:
            return None
        while stack:
            curr.next = stack.pop()
            curr = curr.next
        curr.next=None
        return headn
