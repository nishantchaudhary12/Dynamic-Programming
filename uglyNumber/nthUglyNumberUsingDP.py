#ugly numbers using dynamic programming


def nthUglyNumber(n: int) -> int:
    count = 1
    curr_2 = 0
    curr_3 = 0
    curr_5 = 0
    ugly = [1]
    while count != n:
        currUgly = min(ugly[curr_2] * 2, ugly[curr_3] * 3, ugly[curr_5] * 5)
        ugly.append(currUgly)
        count += 1
        if currUgly == ugly[curr_2] * 2:
            curr_2 += 1
        if currUgly == ugly[curr_3] * 3:
            curr_3 += 1
        if currUgly == ugly[curr_5] * 5:
            curr_5 += 1
    return ugly[-1]


n = 7
print(nthUglyNumber(n))