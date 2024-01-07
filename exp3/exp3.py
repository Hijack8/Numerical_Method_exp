import struct
import numpy as np

# 函数用于扩展压缩矩阵
# compressed_matrix: 压缩矩阵
# p, q: 用于确定压缩矩阵结构的参数
def expand_compressed_matrix(compressed_matrix, p, q):
    # 调整压缩矩阵的每个元素
    for i in range(p):
        for j in range(p + q + 1):
            if(j < p + i + 1):
                compressed_matrix[i][j] = compressed_matrix[i][j + q - i]
            else:
                compressed_matrix[i][j] = 0
    # 创建一个新的扩展矩阵
    n = len(compressed_matrix)
    expanded_matrix = np.zeros((n, n))

    # 填充扩展矩阵
    for i in range(n):
        start_index = max(0, i - p)
        end_index = min(n, i + q + 1)
        length = end_index - start_index
        expanded_matrix[i, start_index:end_index] = compressed_matrix[i, :length]

    return expanded_matrix

# 读取.dat文件的函数
def read_dat_file(filename):
    with open(filename, 'rb') as file:
        # 解析文件信息
        file_info_format = '3l'
        file_info = struct.unpack(file_info_format, file.read(struct.calcsize(file_info_format)))
        id, ver, id1 = file_info

        # 解析头信息
        head_info_format = '3l'
        head_info = struct.unpack(head_info_format, file.read(struct.calcsize(head_info_format)))
        n, q, p = head_info
        matrix = []
        # 根据版本号处理矩阵
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

        # 如果是压缩矩阵，进行扩展
        if ver == 0x202:
            matrix = expand_compressed_matrix(matrix, p, q)

        # 读取常数项
        constants_format = f'{n}f'
        constants = struct.unpack(constants_format, file.read(struct.calcsize(constants_format)))

        constants = np.array(constants)

    return matrix, constants, q, p

# 高斯消元法求解线性方程组
def gauss_elimination(A, b, p, q):
    n = len(A)
    # 进行前向消元
    for i in range(n):
        for j in range(i+1, min(i+p+1, n)):
            factor = A[j][i] / A[i][i]
            for k in range(i, min(i+q+1, n)):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    x = np.zeros(n)
    # 进行回代
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, min(i+q+1, n)):
            x[i] -= A[i][j] * x[j]
        x[i] = x[i] / A[i][i]

    return x

# 解决方程组的函数
def solve(filename):
    matrix, constants, q, p = read_dat_file(filename)
    x = gauss_elimination(matrix, constants, q, p)
    print(filename + " result:")
    print(x)

# 主函数
def main():
    solve("data20231.dat")
    solve("data20232.dat")
    solve("data20233.dat")
    solve("data20234.dat")
    # solve("data20235.dat")

# 当脚本被直接运行时，执行main函数
if __name__ == '__main__':
    main()
