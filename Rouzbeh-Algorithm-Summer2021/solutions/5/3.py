import random

result = ''


def single_add(a, b, cin):
    s = a + b + cin
    return s % 2, s // 2


def extend(num: str, length):
    return '0' * (length - len(num)) + num


def full_add(binary1, binary2, cin):
    global result
    if len(binary1) == len(binary2) == 0:
        if cin == 1:
            result += '1'
        return
    s, carry = single_add(int(binary1[-1]), int(binary2[-1]), cin)
    full_add(binary1[:-1], binary2[:-1], carry)
    result += str(s)


def generate_two_binaries_and_carry():
    first_left_zeroes = random.randint(0, 3)
    second_left_zeroes = random.randint(0, 3)
    b1 = first_left_zeroes * '0' + bin(random.randint(1, 256))[2:]
    b2 = second_left_zeroes * '0' + bin(random.randint(1, 256))[2:]
    return b1, b2, 0


if __name__ == '__main__':
    x, y = map(lambda k: k.lstrip('0'), input().split())
    max_len = max(len(x), len(y))
    full_add(extend(x, max_len), extend(y, max_len), 0)
    print(result)
