# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        # if not root and not subRoot:
        #     return True
        # if not subRoot and root:
        #     return True
        if not subRoot:
            return True
        if (not root and subRoot):
            return False
        
        left,right=False,False
        if self.sameTree(root,subRoot):
            return True
        else:
            #if the current root doesn't have the same structure, then we keep searching the left and right
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def sameTree(self,root1, root2):
            if not root1 and not root2:
                return True
            if (not root1 and root2) or (not root2 and root1):
                return False
            if root1.val!=root2.val:
                return False
            left=self.sameTree(root1.left, root2.left)
            right=self.sameTree(root1.right, root2.right)
            return (left and right)


