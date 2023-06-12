class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True 
        return self.checkSymmetry(root.left, root.right)

    def checkSymmetry(self, right, left):
        if left is None and right is None:
            return True 
        if left is None or right is None or left.val != right.val:
            return False
        return self.checkSymmetry(left.left, right.right) and self.checkSymmetry(right.left, left.right) 