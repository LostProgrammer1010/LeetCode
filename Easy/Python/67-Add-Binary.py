def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            for i in range(len(a)-len(b)):
                b = "0" + b
        else:
            for i in range(len(b)-len(a)):
                a = "0" + a
                
        bl = list(b)
        al = list(a)
        carry = 0
        for i in range(len(b)-1, -1, -1):

            if carry == 1:
                if bl[i] == "0" and al[i] == "1":
                    al[i] = "0"
                elif bl[i] == "0" and al[i] == "0":
                    carry = 0
                    al[i] = "1"
            else:
	            if bl[i] == "1" and al[i] == "1":
	                    carry = 1
	                    al[i] = "0"
	                elif bl[i] == "1" and al[i] == "0":
	                    al[i] = "1"

        if carry == 1:
            al.insert(0, "1")

        return "".join(al)
