import math

phi = (1 + math.sqrt(5)) / 2

def is_p_position(m, n):
    k = abs(m - n)
    if (m == math.floor(k * phi) and n == math.floor(k * phi) + k) or (m == math.floor(k * phi) + k and n == math.floor(k * phi)):
        return True
    
    return False

# test code
def main():
    m = int(input("Enter the first number (m): "))
    n = int(input("Enter the second number (n): "))

    board = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if is_p_position(i, j):
                board[i][j] = 0

    for row in board:
        print(" ".join(str(x) for x in row))

if __name__ == "__main__":
    main()
