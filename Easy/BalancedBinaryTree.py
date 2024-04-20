def isBalanced(root: Optional[TreeNode]) -> bool:
    return Height(root) >= 0

def Height(root) -> int:
    if root is None: return 0

    left, right = Height(root.left), Height(root.right)


    if left < 0 or right < 0 or abs(left - right) > 1: return -1

    return max(left, right) + 1
