# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        def helper(root: TreeNode, result: list):
            if root is None:
                return
            helper(root.left, result)
            result.append(root.val)
            helper(root.right, result)

        result = []
        helper(root, result)
        return result

c = TreeNode(3, None, None)
b = TreeNode(2, c, None)
a = TreeNode(1, None, b)
sol = Solution()
print(sol.inorderTraversal(a))