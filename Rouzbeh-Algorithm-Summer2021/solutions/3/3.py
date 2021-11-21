def reverse_fib(n0, n1):
    if n0 == 0:
        # Base case
        return
    print(n0)
    reverse_fib(n1 - n0, n0)


x0 = int(input())
x1 = int(input())
reverse_fib(x0, x1)