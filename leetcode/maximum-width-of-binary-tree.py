# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        width = defaultdict(list)

        def backtrack(root,lv,lv_count):

            if not root:
                return
            width[lv].append(lv_count)

            backtrack(root.left,lv+1,2*lv_count + 1)

            backtrack(root.right,lv+1,2*lv_count + 2)

        backtrack(root,0,0)

        ans = 0
        for key,val in width.items():

            ans = max(ans, max(val)-min(val)+1)
        return ans
    