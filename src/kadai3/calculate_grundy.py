import is_p_position

def calculate_grundy(n):
    board = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    # calculate the Grundy number for P positions
    for i in range(n + 1):
        for j in range(n + 1):
            if is_p_position.is_p_position(i, j):
                board[i][j] = 0
            else:
                board[i][j] = -1

    # calculate the Grundy numbers for non-P positions
    print("Calculate Grundy numbers")
    for i in range(1, 2 * n + 1):
        print(f"i = {i}") # debug output
        if i <= n: # proceed for the rows
            for j in range(i + 1):
                print(f"check board[{i - j}][{j}]") # debug output
                if board[i - j][j] == -1:
                    grundy_set = set()
                    # search left, up, and leftUp for Grundy numbers
                    for k in range(1, i - j + 1):
                        # up
                        if k <= n and board[i - j - k][j] != -1:
                            grundy_set.add(board[i - j - k][j])
                    for k in range(j + 1):
                        # left
                        if k <= n and board[i - j][k] != -1:
                            grundy_set.add(board[i - j][k])
                    for k in range(1, min(i - j, j) + 1):
                        # leftUp
                        if k <= n and board[i - j - k][j - k] != -1:
                            grundy_set.add(board[i - j - k][j - k])

                    # calculate the minimum excludant (mex)
                    mex = 0
                    while mex in grundy_set:
                        mex += 1

                    board[i - j][j] = mex # set the Grundy number

        else: # proceed for the columns
            for j in range(2 * n - i + 1):
                grundy_set = set()
                # search left, up, and leftUp for Grundy numbers
                if board[n + 1 - j][i - n + j] != -1:
                    for k in range(1, n + 1 - j + 1):
                        # up
                        if i - j - k >= 0 and board[i - j - k][j] != -1:
                            grundy_set.add(board[i - j - k][j])
                    for k in range(1, i - n + j + 1):
                        # left
                        if j - k >= 0 and board[i - j][j - k] != -1:
                            grundy_set.add(board[i - j][j - k])
                    for k in range(1, min(n + 1 - j, i - n + j) + 1):
                        # leftUp
                        if i - j - k >= 0 and j - k >= 0 and board[i - j - k][j - k] != -1:
                            grundy_set.add(board[i - j - k][j - k])

                    # calculate the minimum excludant (mex)
                    mex = 0
                    while mex in grundy_set:
                        mex += 1

                    board[i - j][j] = mex  # set the Grundy number

    return board

# test code
def main():
    n = int(input("Enter the size of the board (n): "))

    board = calculate_grundy(n)

    for row in board:
        print(" ".join(str(x) for x in row))

if __name__ == "__main__":
    main()