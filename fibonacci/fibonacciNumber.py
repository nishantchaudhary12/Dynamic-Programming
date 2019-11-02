#fibonacci numbers


def fibonacci(N):
    count = 1
    i = 0
    j = 1
    if N == 0:
        return 0
    else:
        while count != N:
            temp = i + j
            i = j
            j = temp
            count += 1
        return j
    

num = 30
print(fibonacci(num))