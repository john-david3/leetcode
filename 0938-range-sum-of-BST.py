# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        inRange = []
        self.postorder(root, inRange, low, high)
        total = sum(inRange)
        return total

    def postorder(self, node: TreeNode, inRange: list, low:int, high:int):
        if not node:
            return
        self.postorder(node.left, inRange, low, high)
        self.postorder(node.right, inRange, low, high)
        if node.val >= low and node.val <= high:
            inRange.append(node.val)

if __name__ == "__main__":
    s = Solution()
    f = TreeNode(18,None,None)
    e = TreeNode(7,None,None)
    d = TreeNode(3,None,None)
    c = TreeNode(15,None,f)
    b = TreeNode(5,d,e)
    a = TreeNode(10,b,c)
    print(s.rangeSumBST(root = a, low = 7, high = 15))