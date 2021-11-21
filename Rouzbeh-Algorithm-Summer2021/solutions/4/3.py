def hanoi(start, temp, end, n):
    if n == 1:
        print(f'move 1 from {start} to {temp}')
        print(f'move 1 from {temp} to {end}')
    else:
        hanoi(start, temp, end, n - 1)
        print(f'move {n} from {start} to {temp}')
        hanoi(end, temp, start, n - 1)
        print(f'move {n} from {temp} to {end}')
        hanoi(start, temp, end, n - 1)


x = int(input())
hanoi('A', 'B', 'C', x)
