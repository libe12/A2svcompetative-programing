# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        frequency = defaultdict(int)

        def maxof(root):
            nonlocal frequency 

            if not root:
                return 
        
            frequency[root.val] += 1

            return maxof(root.left) or maxof(root.right)
       
        maxof(root)
        max_of = max(frequency.values())
       
        ans = []
        for key,val in frequency.items():
            if val == max_of:
                ans.append(key)
        return ans