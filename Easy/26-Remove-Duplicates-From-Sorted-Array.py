def removeDuplicates(self, nums: List[int]) -> int:
        length_nums = len(nums)

        i = 0
        new_space = 0

        while(i < length_nums):
            cur_val = nums[i]
            nums[new_space] = cur_val
            new_space +=1

            while(i < length_nums and nums[i] == cur_val):
                i += 1

        return new_space
