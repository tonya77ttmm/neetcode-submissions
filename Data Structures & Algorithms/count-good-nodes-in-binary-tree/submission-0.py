# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #return how many good nodes are in this subtree
        # if not root:
        #     return 0
        # left=goodNodes(root.left)
        # right=goodNodes(root.right)
        self.res=0
        def dfs(root,max_value_pth):
            if not root:
                return 
            if root.val>=max_value_pth:
                self.res+=1
                max_value_pth=max(root.val,max_value_pth)
            dfs(root.left,max_value_pth)
            dfs(root.right,max_value_pth)
        dfs(root, root.val)
        return self.res
        
        #left+right

        