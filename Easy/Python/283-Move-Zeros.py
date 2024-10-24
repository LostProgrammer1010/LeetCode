def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0

        while(count != len(nums)-1):
            if nums[i] == 0:
                x = i
                while(x != len(nums)-1):
                    nums[x], nums[x+1] = nums[x+1], nums[x]
                    x += 1
            else:
                i += 1

            count += 1
