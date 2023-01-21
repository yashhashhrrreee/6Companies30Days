# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        array = []
        def bst_to_list(root,array):
            if root:
                bst_to_list(root.left, array)
                array.append(root.val)
                bst_to_list(root.right, array)


        
        bst_to_list(root1,array)
        bst_to_list(root2,array)
        return sorted(array)
