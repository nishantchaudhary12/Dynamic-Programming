def isUgly(num):
    if num > 0 and num < 7:
        return True
    else:
        i = 2
        while i <= num:
            if i > 5:
                break
            while num % i == 0:
                num //= i
            i += 1
        if num == 1:
            return True
        else:
            return False


def nthUglyNumber(n: int) -> int:
    count = 0
    i = 1
    while count != n:
        if isUgly(i):
            count += 1
        i += 1
    return i - 1


n = 5
print(nthUglyNumber(5))