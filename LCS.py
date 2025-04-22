def lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    # Create a 2D DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp table bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Recover the LCS from dp table
    i, j = m, n
    lcs_str = []
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs_str)), dp[m][n]


# ------------------- DRIVER CODE -------------------
def main():
    X = input("Enter first string: ")
    Y = input("Enter second string: ")

    result, length = lcs(X, Y)

    print(f"\nLongest Common Subsequence: {result}")
    print(f"Length of LCS: {length}")


if __name__ == "__main__":
    main()
