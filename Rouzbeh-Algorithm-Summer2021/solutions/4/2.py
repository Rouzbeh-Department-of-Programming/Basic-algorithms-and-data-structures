def climbing_ways(n):
    if n == 0:
        # Base case 1
        return 1
    if n < 0:
        # Don't forget this case!
        return 0
    return climbing_ways(n - 1) + climbing_ways(n - 2) + climbing_ways(n - 5)


print(climbing_ways(int(input())))
