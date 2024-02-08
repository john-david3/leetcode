# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        def _preorder(root: TreeNode, array: list):
            if root == None:
                return
            array.append(root.val)
            _preorder(root.left, array)
            _preorder(root.right, array)

        array = []
        _preorder(root, array)
        return array
        