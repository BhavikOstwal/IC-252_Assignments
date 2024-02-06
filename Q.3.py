import numpy as np

mat= np.array([[1,3,4,5,2],[1,5,2,4,3],[5,2,3,4,1,],[1,4,2,6,9],[4,5,2,1,7]])
def left_diagonal_sum(mat:np.ndarray)->float:
    sum = 0
    for i in range(len(mat[0])):
        sum += mat[i][i]
    return sum

def right_diagonal_sum(mat:np.ndarray)->float:
    sum = 0
    n = len(mat[0])
    for i in range(n):
        sum += mat[i][n-i-1]
    return sum

print(f"Left Diagonal Sum of\n{mat} is {left_diagonal_sum(mat)}")
print(f"Right Diagonal Sum of\n{mat} is {right_diagonal_sum(mat)}")

def submatrix_3x4(mat: np.ndarray)-> np.ndarray:
    return mat[:3, 1:5]

print(f"The desired submatrix of\n {mat}\n is a {submatrix_3x4(mat).shape} matrix: \n {submatrix_3x4(mat)}")