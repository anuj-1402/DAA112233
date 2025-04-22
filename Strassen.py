# to multiply two matrices
def multiply(arr, brr):
    n = len(arr)

    # to store the resultant matrix
    res = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += arr[i][k] * brr[k][j]

    return res

if __name__ == "__main__":
    arr = [[7, 8], [2, 9]]
    brr = [[14, 5], [5, 18]]
    res = multiply(arr, brr)
    for i in range(len(res)):
        for j in range(len(res[i])):
            print(res[i][j], end=" ")
        print()
