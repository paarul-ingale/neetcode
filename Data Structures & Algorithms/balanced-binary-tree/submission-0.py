# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(node):
            if node is None:
                return 0

            left = balanced(node.left)
            right = balanced(node.right)

            # Step 1: If either subtree is unbalanced,
            if left==-1 or right==-1:
                return -1
            # Step 2: Check the height difference
            if abs(left - right) > 1:
                return -1

            # Step 3: Return current subtree height
            return max(left,right)+1

        return balanced(root) != -1