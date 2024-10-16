def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        if target <= nums[start]:
            return start
        elif target > nums[end]:
            return end + 1
        elif target >= nums[end]:
            return end
        
        while(start <= end):
            middle = start + (end - start) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target and (middle != 0 and nums[middle - 1] < target):
                return middle
            elif nums[middle] < target and (middle < len(nums) and nums[middle + 1] > target):
                return middle + 1

            elif nums[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
