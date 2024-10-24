def myAtoi(self, s: str) -> int:
    negative = False
    start = False
    integer = ("1","2","3","4","5","6","7","8","9","0")

    final_integer = list()
    s = s.strip()
    number = 0

    for i in range(len(s)):
        if s[i] not in integer:
            break

        if start and s[i] in integer:
            final_integer.append(s[i])

        if not start and s[i] in integer:
            start = True
            final_integer.append(s[i])

        if s[i] == "-" and not start and not negative:
            negative = True
            start = True
        elif s[i] == "+" and not start:
            start = True
        elif s[i] not in integer:
            break
        

    for i in final_integer:
        number = int(i) + number * 10

    if negative: number = number * -1

    if number > 2**31 -1: return 2**31 -1
    if number < -2**31:return -2**31

    if not final_integer: return 0
    else:return number


