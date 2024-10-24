ans = 0

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:

    helper(root)
    return ans


def helper(root: Optional[TreeNode]) -> int:

    if root is None:
        return 0

    left = helper(root.right)
    right = helper(root.left)
    ans = max(ans, left+right)
    return max(left, right) + 1
