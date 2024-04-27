def last_fib_digit(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append((fib[i-1] + fib[i-2]) % 10)
    return fib[n-1] % 10