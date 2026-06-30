# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2):
            if not root1 and not root2:
                return True
            if (not root1 and root2) or (not root2 and root1):
                return False
            if root1.val!=root2.val:
                return False
            left=sameTree(root1.left, root2.left)
            right=sameTree(root1.right, root2.right)
            return (left and right)
        
        if not root and not subRoot:
            return True
        if (not root and subRoot):
            return False
        if not subRoot and root:
            return True
        left,right=False,False
        if root.val==subRoot.val:
            left=sameTree(root.left,subRoot.left)
            right=sameTree(root.right,subRoot.right)
        if left and right:
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)



