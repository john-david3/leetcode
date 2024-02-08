# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        def _postorder(root: TreeNode, array: list) -> None:
            if root == None:
                return
            _postorder(root.left, array)
            _postorder(root.right, array)
            array.append(root.val)
            
        array = []
        _postorder(root, array)
        return array