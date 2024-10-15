def convertToTitle(self, columnNumber: int) -> str:

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    conventions = ""

    while(columnNumber > 0):
        remainder = (columnNumber-1) % 26

        
        conventions = alpha[remainder] + conventions


        columnNumber = (columnNumber-1) // 26

    return conventions
