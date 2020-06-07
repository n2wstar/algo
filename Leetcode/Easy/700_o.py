# 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root : 
            if root.val == val : return root
            elif root.val < val : return self.searchBST(root.right,val)
            else : return self.searchBST(root.left,val)
        else: return None