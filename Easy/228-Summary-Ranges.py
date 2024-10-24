def summaryRanges(self, nums: List[int]) -> List[str]:
        s_range = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i < len(nums)-1 and nums[i] + 1 == nums[i+1]:
                i += 1

            if start != nums[i]:
                s_range.append(f"{start}->{nums[i]}")
            else:
                s_range.append(f"{start}")

            i += 1

        return s_range
    
