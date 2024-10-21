def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(j for j in jewels)
        counter = 0

        for i in stones:
            if i in jewels_set:
                counter += 1

        return counter
