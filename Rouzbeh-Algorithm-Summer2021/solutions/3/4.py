def tiling(n):
    if n in [1, 2]:  # To shorten the base cases if statement, you can use this notation: if n in [base1, base2, ...]
        # Base case
        return n
    return tiling(n - 1) + tiling(n - 2)


x = int(input())
print(tiling(x))
