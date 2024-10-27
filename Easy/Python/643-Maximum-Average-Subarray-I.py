def findMaxAverage(self, nums: List[int], k: int) -> float:

        l , r = 0, k-1
        avg_max = -2**32

        total = sum(nums[l:r+1])

        while(r < len(nums)):
            average = total / k
            if average > avg_max:
                avg_max = average
            total -= nums[l]
            l += 1
            r += 1
            if r < len(nums):
                total += nums[r]
        return avg_max
