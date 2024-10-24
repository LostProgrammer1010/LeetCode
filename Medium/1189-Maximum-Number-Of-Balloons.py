def maxNumberOfBalloons(self, text: str) -> int:

        counter_text = Counter(text)

        counter = 0 

        while(True):

            for i in "balloon":
                if i not in counter_text or counter_text[i] == 0:
                    return counter
                counter_text[i] -= 1

            counter += 1
