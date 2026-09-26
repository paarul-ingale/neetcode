# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        ten = 1
        no1 = 0
        while curr1:
            no1 += ten * curr1.val
            ten*= 10
            curr1 = curr1.next
        curr2 = l2
        ten = 1
        no2 = 0
        while curr2:
            no2 += ten * curr2.val
            ten*=10
            curr2 = curr2.next

        summation = no1 +no2
        head = ListNode(summation%10)
        curr = head
        summation //= 10

        while summation>0:
            
            curr.next = ListNode(summation%10)
            curr = curr.next
            summation //= 10
            

        return head
