#fibonacci numbers


def fibonacci(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return fibonacci(N - 1) + fibonacci(N - 2)


num = 30
print(fibonacci(num))