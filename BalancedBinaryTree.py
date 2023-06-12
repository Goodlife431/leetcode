class Solution:
    def isBalanced(self, root):
        if root is None:
            return True
        return self.checkBalanced(root) != -1
    
    def checkBalanced(self, node):
        if node is None:
            return 0
        
        left_height = self.checkBalanced(node.left)
        if left_height == -1:
            return -1
        
        right_height = self.checkBalanced(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
