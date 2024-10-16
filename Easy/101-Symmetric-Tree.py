def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)

def helper(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:

        if left is None and right is None:
            return True

        if bool(left is None) ^ bool(right is None) or left.val != right.val:
            return False

        return self.helper(left.left, right.right) and self.helper(left.right, right.left)
