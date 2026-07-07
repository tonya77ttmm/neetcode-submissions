# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result=float("-inf")

        #max pathSum could be left child +right child +cur 
        def dfs(root)->int: 
            #max pathsum that passes through this node
            if not root:
                return 0
            pathsum=root.val
            left=dfs(root.left)
            right=dfs(root.right)
            pathsum+=left if left>0 else 0
            pathsum+=right if right>0 else 0
            self.result=max(self.result, pathsum)
            return root.val+max(0,left,right)

        dfs(root)
        return self.result