def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            match i:
                case "+": stack.append(stack[len(stack)-1] + stack[len(stack)-2])
                case "D": stack.append(stack[len(stack)-1]*2)
                case "C": stack.pop()
                case _: stack.append(int(i))

        return sum(stack)
