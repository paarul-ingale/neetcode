"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        if not head:
            return None
        curr_ref = head
        new_head = Node(head.val)
        curr = new_head
        d[curr_ref] = curr
        curr_ref = curr_ref.next
        

        while curr and curr_ref:
            new_node = Node(curr_ref.val)
            curr.next = new_node
            curr = curr.next
            d[curr_ref]=curr
            curr_ref = curr_ref.next
        curr = new_head 
        curr_ref = head
        while curr:
            if curr_ref.random:
                curr.random = d[curr_ref.random]
            else:
                curr.random = None
            curr = curr.next
            curr_ref = curr_ref.next
        return new_head
