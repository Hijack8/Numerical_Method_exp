import struct
import numpy as np

def expand_compressed_matrix(compressed_matrix, p, q):
    for i in range(p):
        for j in range(p + q + 1):
            if(j < p + i + 1):
                compressed_matrix[i][j] = compressed_matrix[i][j + q - i]
            else:
                compressed_matrix[i][j] = 0
    n = len(compressed_matrix)
    expanded_matrix = np.zeros((n, n))

    for i in range(n):
        start_index = max(0, i - p)
        end_index = min(n, i + q + 1)
        length = end_index - start_index
        expanded_matrix[i, start_index:end_index] = compressed_matrix[i, :length]

    return expanded_matrix
def read_dat_file(filename):
    with open(filename, 'rb') as file:
        file_info_format = '3l'
        file_info = struct.unpack(file_info_format, file.read(struct.calcsize(file_info_format)))
        id, ver, id1 = file_info

        head_info_format = '3l'
        head_info = struct.unpack(head_info_format, file.read(struct.calcsize(head_info_format)))
        n, q, p = head_info
        matrix = []
        if ver == 0x102:
            for _ in range(n):
                row_format = f'{n}f'
                row = struct.unpack(row_format, file.read(struct.calcsize(row_format)))
                matrix.append(row)
        elif ver == 0x202:
            bandwidth = q + p + 1
            for _ in range(n):
                row_format = f'{bandwidth}f'
                row = struct.unpack(row_format, file.read(struct.calcsize(row_format)))
                matrix.append(row)

        matrix = np.array(matrix)

        if ver == 0x202:
            matrix = expand_compressed_matrix(matrix, p, q)

        constants_format = f'{n}f'
        constants = struct.unpack(constants_format, file.read(struct.calcsize(constants_format)))

        constants = np.array(constants)

    return id, ver, id1, matrix, constants, q, p

def gauss_elimination(A, b, p, q):
    n = len(A)
    for i in range(n):
        for j in range(i+1, min(i+p+1, n)):
            factor = A[j][i] / A[i][i]
            for k in range(i, min(i+q+1, n)):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, min(i+q+1, n)):
            x[i] -= A[i][j] * x[j]
        x[i] = x[i] / A[i][i]

    return x
def main():
    filename = 'data20234.dat'
    id, ver, id1, matrix, constants, q, p = read_dat_file(filename)
    x = gauss_elimination(matrix, constants, q, p)
    print(x)

if __name__ == '__main__':
    main()