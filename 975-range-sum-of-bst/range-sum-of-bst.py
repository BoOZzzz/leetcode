# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        #exclude
        if root.val < low: #move right
            return self.rangeSumBST(root.right, low, high)
        if root.val > high: #move left
            return self.rangeSumBST(root.left, low, high)
        

        #adding recursively
        return (root.val # current value
        + self.rangeSumBST(root.left, low, high) #add left subtree recursively
        + self.rangeSumBST(root.right, low, high) #add right subtree recursively
        )


        