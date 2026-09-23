# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow =slow.next
            fast = fast.next.next
        middle = slow
        head2 = middle.next
        middle.next = None

        
        prev = None
        while head2:
            n_node = head2.next
            head2.next = prev
            prev = head2
            head2 = n_node

        head1 = head
        head2 = prev

        while head1 and head2:
            next1 = head1.next
            next2 = head2.next
            head1.next = head2
            head2.next = next1
            head2 = next2
            head1 = next1
        



