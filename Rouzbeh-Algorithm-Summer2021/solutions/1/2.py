def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


result = int(input())
b = int(input())
for j in range(result, b + 1):
    if is_prime(j):
        print(j)

