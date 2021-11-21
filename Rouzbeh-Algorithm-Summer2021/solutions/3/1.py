def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def selection_sort(lst):
    for i in range(len(lst)):
        max_index = i
        for j in range(i, len(lst)):
            if lst[j] > lst[max_index]:
                max_index = j
        swap(lst, i, max_index)


def get_duplicates(lst):
    result = []
    selection_sort(lst)
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            result.append(lst[i])
    return result


a = list(map(int, input().split()))
b = get_duplicates(a)
for i in range(len(b)):
    if i == 0:
        print(b[0], end=" ")
        continue
    if b[i] != b[i - 1]:
        print(b[i], end=" ")
