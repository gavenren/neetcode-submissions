# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left_height = self.checkHeight(root.left)
        right_height = self.checkHeight(root.right)
        if abs(left_height - right_height) > 1 or self.isBalanced(root.left) is False or self.isBalanced(root.right) is False:
            return False
        else:
            return True
                    
    def checkHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.checkHeight(root.left)
        right_height = self.checkHeight(root.right)
        return 1 + max(left_height, right_height)