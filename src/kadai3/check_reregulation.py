from calculate_grundy import calculate_grundy
from print_board import print_board

def check_reregulation(board):
    for row in board:
        for scycle in range(1, 11):
            print(f"Checking row: {row} with scycle: {scycle}")

            for top in range(0, len(row)):
                print(f"Check reregulation start at {top}")
                i = 0

                while top + (i + 1) * scycle < len(row):
                    f_loop = row[top + i * scycle: top + (i + 1) * scycle]
                    s_loop = row[top + (i + 1) * scycle: top + (i + 2) * scycle]
                    diff_loop = [s_loop[j] - f_loop[j] for j in range(scycle)]
                    print(f"diff_loop: {diff_loop}")

                    i += 1  

def main():
    n = int(input("Input the size of the board (n + 1): "))

    board = calculate_grundy(n)

    print_board(board)

    check_reregulation(board)

if __name__ == "__main__":
    main()