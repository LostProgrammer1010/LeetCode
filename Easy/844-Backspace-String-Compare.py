def backspaceCompare(self, s: str, t: str) -> bool:

        s_val = ""
        t_val = ""
        backspace = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == "#":
                backspace += 1
            elif backspace > 0:
                backspace -= 1
            else:
                s_val = s[i] + s_val

        backspace = 0

        for i in range(len(t)-1, -1, -1):
            if t[i] == "#":
                backspace += 1
            elif backspace > 0:
                backspace -= 1
            else:
                t_val = t[i] + t_val


        return s_val == t_val
