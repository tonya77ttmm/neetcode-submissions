# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        val=preorder[0]
        root=TreeNode(val)
        p=inorder.index(val)
        # leftmost=p-1
        # rightleast=p+1

        # lm=0
        # while preorder[lm]!=inorder[leftmost]:
        #     lm+=1
        
        root.left=self.buildTree(preorder[1:p+1],inorder[0:p])
        root.right=self.buildTree(preorder[p+1:], inorder[p+1:])
        return root