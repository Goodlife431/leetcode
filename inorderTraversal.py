# Given the root of a binary tree, return the inorder traversal of its nodes' values.

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def inorder(node): 
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)
            
        inorder(root)
        return result 