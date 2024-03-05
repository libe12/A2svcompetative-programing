# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            maxval = -float('inf')
            minval = float('inf')

            if not root.left and not root.right:
                return (root.val , root.val)
            if root.left:
                left = dfs(root.left)
                val = max( abs( root.val - left[0] ) , abs(root.val - left[1]))
                ans = max(ans , val)
                maxval = max(left[1] ,  root.val , maxval)
                minval = min(left[0] ,  root.val, minval)

            if root.right:
                right = dfs(root.right)


                val = max((abs(root.val - right[0] ) , abs(root.val - right[1])))
                ans = max(ans , val)

                maxval = max( right[1] , root.val , maxval)
                minval = min( right[0] , root.val , minval)

            return [minval , maxval]
        dfs(root)

        return ans