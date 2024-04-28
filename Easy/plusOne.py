plusOne(digits: List[int]) -> List[int]:
    remainder = 1
    idx = len(digits) - 1

    while(remainder > 0):
        if idx == 0 and digits[idx] == 9:
            digits[idx] = 0
            digits.insert(0, 1)
            remainder = 0
        elif digits[idx] == 9:
            digits[idx] = 0
        else:
            digits[idx] += 1
            remainder = 0
        idx -= 1

    return digits
