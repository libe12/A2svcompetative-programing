# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node,right,left):
            if not node:
                return True
            if  not(node.val > left and node.val < right):
                return False
            return valid(node.left,node.val,left) and valid(node.right,right,node.val)
        return valid(root,float('inf'),float('-inf'))