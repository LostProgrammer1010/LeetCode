def removeElement(self, nums: List[int], val: int) -> int:
        start = 0 
        end = len(nums) - 1
        k = 0
        
        while(start <= end):
            if nums[start] != val:
                k+=1
            if nums[start] == val:
                swap = False
                while start <= end and not swap:
                    if nums[end] != val:
                        temp = nums[end]
                        nums[end] = nums[start]
                        nums[start] = temp
                        swap = True
                        k += 1
                    end -= 1
            start += 1
            
        return k
