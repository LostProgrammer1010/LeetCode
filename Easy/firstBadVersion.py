def firstBadVersion(self, n: int) -> int:
    start = 1
    end = n + 1
    if isBadVersion(1):
        return 1

    while(end > start):
        mid = start + (end - start) // 2

        if isBadversion(mid):
            if isBadVersion(mid - 1) is False:
                return mid
            end = mid - 1

        else:
            if isBadVersion(mid + 1):
                return mid + 1
            start = mid + 1
