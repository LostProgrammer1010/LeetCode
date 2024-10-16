def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        return self.helper(root, inorder)

def helper(self, root: Optional[TreeNode], inorder: list[int]) -> List[int]:
        if root is not None:
            self.helper(root.left, inorder)
            inorder.append(root.val)
            self.helper(root.right, inorder)
    
        return inorder
