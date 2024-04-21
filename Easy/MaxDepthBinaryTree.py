def maxDepth(root: Optional[TreeNode]) -> int:
    return helper(root, 0)

def helper(root: Optional[TreeNode]), depth: int) -> int:
    if root is None:
        return depth

    return max(helper(root.left, depth + 1), helper(root.right, depth + 1)
