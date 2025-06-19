def print_board(board):
    board_size = len(board)

    print(f"\n{board_size}x{board_size} Wythoff Nim Board:\n")

    # Determine the maximum width needed for formatting
    max_width = 0
    for row in board:
        for x in row:
            max_width = max(max_width, len(str(x)))

    # Print column headers
    header = "    " + " ".join(f"{j:{max_width}}" for j in range(board_size))
    print(header)
    print("---" + " ".join("-" * max_width for _ in range(board_size)))

    for i, row in enumerate(board):
        # Print row index and the row values
        row_str = f"{i:2} | " + " ".join(f"{x:{max_width}}" for x in row)
        print(row_str)

