def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_of_value = []

        for row in matrix:
            if target == row[len(row)-1]:
                return True
            elif target < row[len(row)-1]:
                row_of_value = row
                break

        return target in row_of_value
