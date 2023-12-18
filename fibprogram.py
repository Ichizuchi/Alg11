def fib_td(n, f):
    if n <= 1:
        f[n] = n
    else:
        f[n] = fib_td(n - 1, f) + fib_td(n - 2, f)
    return f[n]


def fib_bu(n):
    f = [-1] * (n + 1)
    f[0] = 0
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


def fib_improved(n):
    if n <= 1:
        return n

    prev, curr = 0, 1

    for i in range(2, n + 1):
        next_val = prev + curr
        prev, curr = curr, next_val
    return curr


def fibonacci(n, calculation_method):
    if calculation_method == 0:
        f = [-1] * (n + 1)
        return fib_td(n, f)
    elif calculation_method == 1:
        return fib_bu(n)
    elif calculation_method == 2:
        return fib_improved(n)
    else:
        print("Неизвестный метод расчета:", calculation_method)
        return -1


if __name__ == "__main__":
    N = 6
    print("Число Фибоначчи(", N, "):")
    print("(", N, ", 0) =", fibonacci(N, 0))
    print("(", N, ", 1) =", fibonacci(N, 1))
    print("(", N, ", 2) =", fibonacci(N, 2))
