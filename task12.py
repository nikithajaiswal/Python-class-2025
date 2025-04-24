def designer_door_mat(N, M):
    """
    Print a door mat of height N (odd) and width 3*N,
    with 'WELCOME' in the center and the .|. motif.
    """
    M = 3 * N
    half_rows = N // 2

    # Top half
    for i in range(half_rows):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, '-'))

    # Middle
    print("WELCOME".center(M, '-'))

    # Bottom half
    for i in range(half_rows - 1, -1, -1):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, '-'))


# Example usage:
if __name__ == "__main__":
    N, M = map(int, input().split())
    designer_door_mat(N, M)