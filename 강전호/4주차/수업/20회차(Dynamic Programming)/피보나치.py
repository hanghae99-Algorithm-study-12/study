memo = {1: 1, 2: 1}


def fibo(n):
    if n in memo:
        return memo[n]

    memo[n] = fibo(n - 1) + fibo(n - 2)
    print(memo)
    return memo[n]
fibo(10)