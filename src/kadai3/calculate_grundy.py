import is_p_position

def calculate_grundy(n):
    """
    Calculate the Grundy numbers for a Wythoff game board of size n x n.
    
    Parameters:
    n (int):
        The size of the board (n x n).
    Returns:
    list:
        A 2D list representing the Grundy numbers for each position on the board.
    """
    board = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    # calculate the Grundy number for P positions
    for i in range(n + 1):
        for j in range(n + 1):
            if is_p_position.is_p_position(i, j):
                board[i][j] = 0
            else:
                board[i][j] = -1

    # calculate the Grundy numbers for non-P positions
    for i in range(1, 2 * n + 1):
        if i <= n: # proceed for the rows
            for j in range(i + 1):
                if board[i - j][j] == -1:
                    grundy_set = set()
                    # search left, up, and leftUp for Grundy numbers
                    for k in range(1, i - j + 1):
                        # up
                        grundy_set.add(board[i - j - k][j])
                    for k in range(j + 1):
                        # left
                        grundy_set.add(board[i - j][k])
                    for k in range(1, min(i - j, j) + 1):
                        # leftUp
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
                if board[n - j][i - n + j] == -1:
                    for k in range(1, n - j + 1):
                        # up
                        grundy_set.add(board[n - j - k][i - n + j])
                    for k in range(1, i - n + j + 1):
                        # left
                        grundy_set.add(board[n - j][i - n + j - k])
                    for k in range(1, min(n - j, i - n + j) + 1):
                        # leftUp
                        grundy_set.add(board[n - j - k][i - n + j - k])

                    # calculate the minimum excludant (mex)
                    mex = 0
                    while mex in grundy_set:
                        mex += 1

                    board[n - j][i - n + j] = mex  # set the Grundy number

    return board

# test code
def main():
    n = int(input("Enter the size of the board (n): "))

    board = calculate_grundy(n)

    for row in board:
        print(" ".join(str(x) for x in row))

if __name__ == "__main__":
    main()