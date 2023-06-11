# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

class Solution:
    def recoverTree(self, root):
        # Variables to store the misplaced nodes
        first, second = None, None
        # Stack for iterative inorder traversal
        stack = []
        # Previous node during inorder traversal
        prev = None

        # Perform iterative inorder traversal
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            # Check if current node is misplaced
            if prev and prev.val > root.val:
                if not first:
                    first = prev
                second = root

            prev = root
            root = root.right

        # Swap the values of the misplaced nodes
        first.val, second.val = second.val, first.val

        return first, second
