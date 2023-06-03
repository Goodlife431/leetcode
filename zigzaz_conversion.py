# def convert(s, num_rows):
#     if num_rows == 1:
#         return s
#     rows = [''] * num_rows
#     current_row = 0
#     direction = -1
#
#     for c in s:
#         rows[current_row] += c
#         if current_row == 0 or current_row == num_rows - 1:
#             direction *= -1
#         current_row += direction
#
#     return ''.join(rows)
#
#
# if __name__ == '__main__':
#     print(convert('palatalising', 3))

def convert(s: str, numRows: int) -> str:
    if numRows < 2 or len(s) <= numRows:
        return s

    rows = [''] * numRows
    row, step = 0, 1

    for char in s:
        rows[row] += char

        if row == 0:
            step = 1
        elif row == numRows - 1:
            step = -1

        row += step

    return ''.join(rows)


if __name__ == '__main__':
    print(convert('palatalising', 3))
