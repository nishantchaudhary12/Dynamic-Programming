#fibonacci numbers


def fibonacci(N):
    arr = [0, 1]
    while len(arr) < N + 1:
        arr.append(0)
    if N <= 1:
        return N
    else:
        if arr[N-1] == 0:
            arr[N-1] = fibonacci(N-1)
        if arr[N-2] == 0:
            arr[N-2] = fibonacci(N-2)

        arr[N] = arr[N-1] + arr[N-2]
        return arr[N]

num = 30
print(fibonacci(num))