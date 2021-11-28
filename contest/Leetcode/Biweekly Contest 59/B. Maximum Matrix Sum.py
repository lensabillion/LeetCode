class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        negtive = 0
        small = float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 0:
                    negtive += 1
                    matrix[i][j] = -1* matrix[i][j]
                if matrix[i][j] < small:
                    small = matrix[i][j]
                    
                total += matrix[i][j]
        if negtive % 2 != 0:
            return total - 2*small
        return total
            