#Напишите функцию для транспонирования матрицы

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = []

def tern(matrix):
    for j in range(len(matrix[0])):
        new_row = []
        for i in matrix:
            new_row.append(i[j])
        transposed_matrix.append(new_row)

def print_matrix(matrix):
    for row in transposed_matrix:
        print(row)

print_matrix(tern(matrix))