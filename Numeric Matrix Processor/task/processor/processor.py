def summa_matrix():
    matrix_sum = []
    n1, m1 = [int(i) for i in input('Enter size of first matrix:').split()]
    print('Enter first matrix:')
    matrix1 = [[float(i) for i in input().split() for _ in range(1)] for _ in range(n1)]
    n2, m2 = [int(i) for i in input('Enter size of second matrix:').split()]
    print('Enter second matrix:')
    matrix2 = [[float(i) for i in input().split() for _ in range(1)] for _ in range(n2)]
    if n1 == n2 and m1 == m2:
        matrix_sum = [[matrix1[j][i] + matrix2[j][i] for i in range(m1)] for j in range(n1)]
        print('The result is:')
        for row in matrix_sum:
            print(' '.join([str(elem) for elem in row]))
    else:
        print('ERROR')


def multiplication_by_number_matrix():
    n1, m1 = [int(i) for i in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix1 = [[float(i) for i in input().split() for _ in range(1)] for _ in range(n1)]
    number = float(input('Enter constant: '))
    matrix_mul = [[matrix1[j][i] * number for i in range(m1)] for j in range(n1)]
    print('The result is:')
    for row in matrix_mul:
        print(' '.join([str(elem) for elem in row]))


def multiplication_matrix_by_matrix():
    n1, m1 = [int(i) for i in input('Enter size of first matrix:').split()]
    print('Enter first matrix:')
    matrix1 = [[float(i) for i in input().split() for _ in range(1)] for _ in range(n1)]
    n2, m2 = [int(i) for i in input('Enter size of second matrix:').split()]
    print('Enter second matrix:')
    matrix2 = [[float(i) for i in input().split() for _ in range(1)] for _ in range(n2)]
    matrix_mul = [[0 for _ in range(m2)] for _ in range(n1)]
    if m1 == n2:
        for i in range(n1):
            for j in range(m2):
                total = 0
                for k in range(m1):
                    total += matrix1[i][k] * matrix2[k][j]
                matrix_mul[i][j] = total
        print('The result is:')
        for row in matrix_mul:
            print(' '.join([str(elem) for elem in row]))
    else:
        print('ERROR')


def transpose_matrix_by_main_diagonal():
    n1, m1 = [int(i) for i in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix1 = [[float(i) for i in input().split() for _ in range(1)] for _ in range(n1)]
    for i in range(n1):
        for j in range(i, m1):
            matrix1[i][j], matrix1[j][i] = matrix1[j][i], matrix1[i][j]
    print('The result is:')
    for row in matrix1:
        print(' '.join([str(elem) for elem in row]))


def transpose_matrix_by_side_diagonal():
    n1, m1 = [int(i) for i in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix1 = [[float(i) for i in input().split() for _ in range(1)] for _ in range(n1)]
    for i in range(n1):
        for j in range(n1 - i, m1):
            if i != n1 - j - 1:
                matrix1[i][j], matrix1[m1 - j - 1][n1 - i - 1] = matrix1[m1 - j - 1][n1 - i - 1], matrix1[i][j]
    print('The result is:')
    for row in matrix1:
        print(' '.join([str(elem) for elem in row]))


def transpose_matrix_by_vertical_line():
    n1, m1 = [int(i) for i in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix1 = [[float(i) for i in input().split() for _ in range(1)] for _ in range(n1)]
    for i in range(n1):
        for j in range(m1 // 2):
            matrix1[i][j], matrix1[i][m1 - j - 1] = matrix1[i][m1 - j - 1], matrix1[i][j]
    print('The result is:')
    for row in matrix1:
        print(' '.join([str(elem) for elem in row]))


def transpose_matrix_by_horizontal_line():
    n1, m1 = [int(i) for i in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix1 = [[float(i) for i in input().split() for _ in range(1)] for _ in range(n1)]
    for i in range(n1 // 2):
        for j in range(m1):
            matrix1[i][j], matrix1[n1 - i - 1][j] = matrix1[n1 - i - 1][j], matrix1[i][j]
    print('The result is:')
    for row in matrix1:
        print(' '.join([str(elem) for elem in row]))


def transpose_matrix():
    print('1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line')
    choice1 = int(input('Your choice: '))
    if choice1 == 1:
        transpose_matrix_by_main_diagonal()
    elif choice1 == 2:
        transpose_matrix_by_side_diagonal()
    elif choice1 == 3:
        transpose_matrix_by_vertical_line()
    elif choice1 == 4:
        transpose_matrix_by_horizontal_line()


def det(n, m, matrix, summa=0, i=0, j=0):
    if n == m == 1:
        summa += matrix[0][0]
        return summa
    else:
        for k in range(m):
            matrix1 = list(matrix)
            matrix1 = matrix1[1:]
            for i in range(len(matrix1)):
                matrix1[i] = matrix1[i][0:k] + matrix1[i][k+1:]
            if k % 2 == 0:
                summa += matrix[0][k] * det(n - 1, m - 1, matrix1)
            else:
                summa -= matrix[0][k] * det(n - 1, m - 1, matrix1)
        return summa


def determinant_matrix():
    n1, m1 = [int(i) for i in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix1 = [[float(i) for i in input().split() for _ in range(1)] for _ in range(n1)]
    print('The result is:\n',  det(n1, m1, matrix1))


def inverse_matrix():
    n1, m1 = [int(i) for i in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix1 = [[float(i) for i in input().split() for _ in range(1)] for _ in range(n1)]
    new_matrix = [[0 for _ in range(n1)] for _ in range(m1)]
    for i in range(n1):
        for j in range(m1):
            matrix = []
            for k in range(n1):
                if k != i:
                    matrix.append([])
                    for t in range(m1):
                        if t != j:
                            matrix[len(matrix) - 1].append(matrix1[k][t])
            if (j + i) % 2 == 0:
                new_matrix[j][i] = det(n1 - 1, m1 - 1, matrix)
            else:
                new_matrix[j][i] = det(n1 - 1, m1 - 1, matrix) * (-1)
    for i in range(n1):
        for j in range(m1):
            new_matrix[i][j] *= 1 / (det(n1, m1, matrix1))
    print('The result is:')
    for row in new_matrix:
        print(' '.join([str(elem) for elem in row]))


choice = 1
while choice != 0:
    print('1. Add matrices\n2. Multiply matrix by a constant'
          '\n3. Multiply matrices\n4. Transpose matrix'
          '\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit')
    choice = int(input('Your choice: '))
    if choice == 1:
        summa_matrix()
    elif choice == 2:
        multiplication_by_number_matrix()
    elif choice == 3:
        multiplication_matrix_by_matrix()
    elif choice == 4:
        transpose_matrix()
    elif choice == 5:
        determinant_matrix()
    elif choice == 6:
        inverse_matrix()
