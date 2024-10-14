def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    if p is None and q is None:
        return True

    if p is None and q is not None:
        return False

    if p is not None and q is None:
        return False

    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
