def productExceptSelf(self, nums: List[int]) -> List[int]:

        l = [1] * len(nums)
        r = [1] * len(nums)

        for i in range(len(nums)-1):
            j = -i - 1
            l[i+1] *= nums[i] * l[i]
            r[j-1] *= nums[j] * r[j]

        return [i*x for i,x in zip(l,r)]
