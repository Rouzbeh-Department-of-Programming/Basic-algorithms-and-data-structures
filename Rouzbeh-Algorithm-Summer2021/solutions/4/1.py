def gcd(a, b):
    if b == 0:
        # Base case
        return a
    # Ask yourself: Does it matter if a > b or b > a ?
    return gcd(b, a % b)  # gcd of a and b equals gcd of b and a % b


n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    print(gcd(x, y))