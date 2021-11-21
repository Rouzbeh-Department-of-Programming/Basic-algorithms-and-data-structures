def print_seven(n):
    width = 2 * n
    if width == 0:
        return

    print('*' * width)
    for i in range(width - 2, -1, -1):
        print(' ' * i + '*')
    print_seven(n - 1)


if __name__ == '__main__':
    x = int(input())
    print_seven(x)
