def pascals_triangle(n: int):
    if n <= 0:
        return
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    # 居中打印
    w = len(' '.join(map(str, triangle[-1])))  # 最后一行宽度作为对齐基准
    for row in triangle:
        print(' '.join(map(str, row)).center(w))

# 示例：输出 10 行
pascals_triangle(10)
