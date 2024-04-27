def multiply_matrices(matrix1, matrix2):
    result = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
                result[i][j] %= 10

    return result

def power_matrix(matrix, n):
    if n == 0:
        return [[1, 0], [0, 1]]  # Identity matrix

    result = [[1, 0], [0, 1]]  # Identity matrix

    while n > 0:
        if n % 2 == 1:
            result = multiply_matrices(result, matrix)
        matrix = multiply_matrices(matrix, matrix)
        n //= 2

    return result

def last_fib_digit(n):
    if n <= 1:
        return n

    matrix = [[1, 1], [1, 0]]
    power = power_matrix(matrix, n - 1)
    return power[0][0] % 10
