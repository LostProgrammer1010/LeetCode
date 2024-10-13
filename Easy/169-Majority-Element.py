def majorityElement(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    return nums[n//2]
