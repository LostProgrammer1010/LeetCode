def countBits(n: int) -> List[int]:
    final = []
    for i in range(0, n+1):
        value = str(bin(i)[2:])
        ones = 0
        for i in value:
            if i == "1":
                ones += 1
        final.append(ones)
    return final
