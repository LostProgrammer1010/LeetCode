def hammingWeight(self, n: int) -> int:
        binary = str(bin(n)[2::])

        one_bits = 0

        for i in binary:
            if i == "1":
                one_bits += 1

        return one_bits
