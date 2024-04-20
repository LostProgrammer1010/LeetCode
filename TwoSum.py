# Works by storing complement of target and current number in a dictionary and see if it exist and returning current number index and complements indexs
def twoSum(nums: List[int], target: int) -> List[int]:
    comp = dict()
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in comp:
            return [i, final.get(difference)]
        comp[nums[i]] = i
