# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #max(left subtree) <root.val and min(right subtree)>root.val
        #and validBST(leftsubtree) and validBST(rightsubtree)
        #left right root

        def dfs(root,min_value,max_value):
            if not root:
                return True
            if root.val<max_value and root.val>min_value:
                left=dfs(root.left,min_value,root.val)
                right=dfs(root.right,root.val,max_value)
                return left and right
            return False
        return dfs(root,float("-inf"),float("inf"))