# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #diameter of current node=max_height(left)+max_height(right)
        if not root:
            return 0
        self.diameter=0
        def dfs_height(root): #height
            if not root:
                return 0
            l_height=dfs_height(root.left)
            r_height=dfs_height(root.right)

            self.diameter=max(self.diameter, l_height+r_height)
            height=max(l_height,r_height)+1

            return height

        dfs_height(root)
        return self.diameter