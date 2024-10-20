def isPossibleToSplit(self, nums: List[int]) -> bool:

        count = Counter(nums)

        for i in count.values():
            if i > 2:
                return False

        return True
