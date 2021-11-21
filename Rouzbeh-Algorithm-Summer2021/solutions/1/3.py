def is_palindromic(number):
    # This function checks if number remains the same whether read forward or backward
    reverse = 0
    temp_num = number
    while number > 0:
        right_digit = number % 10
        number //= 10  # The same as number = number // 10
        reverse *= 10
        reverse += right_digit

    if reverse == temp_num:
        return True
    return False # We don't need else: block. (Why?)


n = int(input())
if is_palindromic(n):
    print("YES")
else:
    print("NO")
