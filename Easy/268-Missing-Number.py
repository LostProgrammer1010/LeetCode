def missingNumber(self, nums: List[int]) -> int:

        nums = sorted(nums)

        for i in range(0, len(nums)-1):
            if nums[i+1] - nums[i] > 1:
                return nums[i] + 1

        if nums[0] == 0:
            return nums[len(nums)-1] + 1
        else:
            return nums[0] - 1
