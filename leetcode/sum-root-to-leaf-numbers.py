# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        ans = []
        
        def helper(root,digit):

            if not root:
                return
            if not root.left and not root.right:
                ans.append(int(digit+str(root.val)))
                return
            helper(root.left, digit+str(root.val))
            helper(root.right, digit +str(root.val))

        helper(root,'')

        print(ans)
        
        return sum(ans)