def reverseBits(n: int) -> int:
    value = bin(n)[2::][::-1]

    while len(value) != 32:
        value = value + "0"

    return int(value, 2)
