# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def count(node):
            nonlocal diameter
            if node is None:
                return 0
    
            left = count(node.left)
            right = count(node.right)

            node_length = right + left
            child_length = max(left, right)+1
            
            diameter = max(diameter, node_length)
            return child_length


        count(root)
        return diameter
