# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def traverse(root):

            if not root:
                return
            if root.val <low or root.val > high:
                pass
            else:
                ans.append(root.val)

            traverse(root.left)
            traverse(root.right)
        ans = []

        traverse(root)

        return sum(ans)

        