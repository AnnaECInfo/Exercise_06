# Exercise 1

def power(a: int, b: int):
    if a <= 0 or b <= 0:
        return -1
    if b == 1:
        return a
    else:
        return int(a * power(a, b - 1))


# Exercise 2


def binary_search(numbers, num: int):
    first = 0
    last = len(numbers) - 1

    if first > last:  # BASE CASE: if the list has been iterated through without finding num, the function returns -1
        return -1

    mid = (first + last) // 2
    if numbers[mid] == num:  # num was found, the function returns its index (num)
        return mid
    elif numbers[mid] > num:  # the value at mid is bigger than num, the function calls itself but sets "mid - 1"
        # as the end of the list to look through
        return binary_search(numbers[:mid - 1], num)
    else:  # the value at mid is smaller than num, the function calls itself but sets "mid + 1"
        # as the beginning of the list to look through
        return binary_search(numbers[mid + 1:], num)
