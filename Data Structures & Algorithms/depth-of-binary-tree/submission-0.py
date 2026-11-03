# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def count(node):
            
            if node is None:
                return 0
    
            left = count(node.left)
            right = count(node.right)

            return 1 + max(left, right)

        return count(root)

