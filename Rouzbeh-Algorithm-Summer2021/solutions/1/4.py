n = int(input())

for i in range(1, n + 1):
    # The first half
    print((n + 1 - i) * " " + i * "*" + (i - 1) * "*")

# The diameter (GHOTR:))
print((2 * n + 1) * "*")

for j in range(1, n + 1):
    # The second half
    print(j * " " + (n + 1 - j) * "*" + (n - j) * "*")
