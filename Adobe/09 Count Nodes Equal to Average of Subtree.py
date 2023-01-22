# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ctr=0
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def recur(root):
            if root is None:
                return [0,0]
            list1=recur(root.left)
            list2=recur(root.right)
            sub_node_sum=list1[0]+list2[0]+root.val
            sub_node_count=list1[1]+list2[1]+1
            if((int(sub_node_sum/sub_node_count))==root.val):
                print(root.val)
                self.ctr+=1
            return [sub_node_sum,sub_node_count]
        recur(root)
        return self.ctr
