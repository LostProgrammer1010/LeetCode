def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0

        for i in range(len(digits)-1, -1, -1):

            if digits[i] == 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += 1
                return digits
 
        if carry == 1:
            digits.insert(0,1)
        

        return digits
