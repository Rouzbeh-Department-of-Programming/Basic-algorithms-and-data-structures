def decimal_to_r(n, r):
    if n == 0:
        return 0
    return n % r + 10 * decimal_to_r(n // r, r)


def r_to_decimal(n, r):
    if n == 0:
        return 0
    return n % 10 + r * r_to_decimal(n // 10, r)


def a_to_b(n, a, b):
    return decimal_to_r(r_to_decimal(n, a), b)


if __name__ == '__main__':
    print(a_to_b(*map(int, input().split())))
