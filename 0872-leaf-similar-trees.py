# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        list1 = []
        list2 = []
        
        self.postorder(root1, list1)
        self.postorder(root2, list2)

        return list1 == list2

    def postorder(self, node: TreeNode, listx: list):
        if not node:
            return
        self.postorder(node.left, listx)
        self.postorder(node.right, listx)
        if not node.left and not node.right:
            listx.append(node.val)

if __name__ == "__main__":
    sol = Solution()
    f = TreeNode(2, None, None)
    e = TreeNode(3, None, None)
    d = TreeNode(1, e, f)
    c = TreeNode(3, None, None)
    b = TreeNode(2, None, None)
    a = TreeNode(1, b, c)
    ans = sol.leafSimilar(d, a)
    print(ans)