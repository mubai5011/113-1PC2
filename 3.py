def gray(array, i, j, value):
    if value != 0:
        array[(i, j)] = value  
def print_sparse_matrix(array, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(array.get((i, j), 0), end=" ")  
        print()
sparse_matrix = {}
gray(sparse_matrix, 0, 1, 50)
gray(sparse_matrix, 1, 3, 120)
gray(sparse_matrix, 2, 4, 180)
gray(sparse_matrix, 3, 2, 255)
print_sparse_matrix(sparse_matrix, 5, 5)