# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def inorderTraversal(node: TreeNode, array: list):
            if node is None:
                return
            array.append(inorderTraversal(node.left, array))
            array.append(node.val)
            array.append(inorderTraversal(node.right, array))

        p_array = []
        inorderTraversal(p, p_array)
        q_array = []
        inorderTraversal(q, q_array)

        print(p_array, q_array)

        return p_array == q_array

e = TreeNode(1, None, None)
d = TreeNode(1, e, None)
b = TreeNode(1, None, None)
a = TreeNode(1, None, b)
sol = Solution()
print(sol.isSameTree(d, a))