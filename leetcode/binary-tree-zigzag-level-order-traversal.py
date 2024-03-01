# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        level = defaultdict(list)

        def levelorder(node,key):
            nonlocal level
            if not node:
                return
            
            level[key].append(node.val)
            
           
            levelorder(node.left,key+1) 
            levelorder(node.right,key+1)

        levelorder(root,0)
        
        ans  = []
        for key,val in level.items():
            if key % 2 == 0:
                ans.append(val)
            else:
                ans.append(val[::-1])
        return ans


        