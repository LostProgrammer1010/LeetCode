def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, columns = len(matrix), len(matrix[0])

        c, r, dc, dr = 0, 0, 1, 0

        solution = []

        for _ in range(rows * columns):
            solution.append(matrix[r][c])
            matrix[r][c] = "."

            if not 0 <= c + dc < columns or not 0 <= r + dr < rows or matrix[r+dr][c+dc] == ".":
                dc, dr = -dr, dc

            r += dr
            c += dc

        return solution
