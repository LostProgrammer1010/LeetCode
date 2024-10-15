def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = []
        columns = []

        for n in range(len(matrix)):
            for m in range(len(matrix[0])):
                if matrix[n][m] == 0:
                    rows.append(n)
                    columns.append(m)

        for row in rows:
            matrix[row] = [0 for i in range(len(matrix[0]))]
        
        for row in range(len(matrix)):
            for column in columns:
                matrix[row][column] = 0
