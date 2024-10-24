def titleToNumber(self, columnTitle: str) -> int:
    columnNumber = 0

    power = 0
    end = len(columnTitle)-1

    while(end >= 0):
        columnNumber += (ord(columnTitle[end])-64) * 26**power
        power += 1
        end -= 1

    return columnNumber
