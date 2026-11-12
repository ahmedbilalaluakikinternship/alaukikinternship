def linear_search(items, target):

    for index, item in enumerate(items):
        if item == target:
            return index

    return -1


def binary_search(numbers, target):

    low = 0
    high = len(numbers) - 1

    while low <= high:

        mid = (low + high) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


def bubble_sort(numbers):

    numbers = numbers.copy()

    for i in range(len(numbers)):

        for j in range(len(numbers) - i - 1):

            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


def merge_sort(numbers):

    if len(numbers) <= 1:
        return numbers.copy()

    mid = len(numbers) // 2

    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result