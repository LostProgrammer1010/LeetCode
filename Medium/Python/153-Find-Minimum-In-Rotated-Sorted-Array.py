def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums)-1

        while(l != r):
            middle = l + (r - l) // 2

            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle

        return nums[r]
