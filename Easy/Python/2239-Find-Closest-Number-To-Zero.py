def findClosestNumber(self, nums: List[int]) -> int:
        smallest = nums[0]

        for i in nums:
            if abs(i) < abs(smallest) or abs(i) == abs(smallest) and i > smallest:
                smallest = i
        
        return smallest
