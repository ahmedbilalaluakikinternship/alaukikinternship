import timeit


numbers = list(range(10000))
target = 9999


def linear_search():
    for index, number in enumerate(numbers):
        if number == target:
            return index

    return -1


def binary_search():
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


linear_time = timeit.timeit(
    linear_search,
    number=1000
)

binary_time = timeit.timeit(
    binary_search,
    number=1000
)

print("Linear Search Time:", linear_time)
print("Binary Search Time:", binary_time)


def bubble_sort(items):
    items = items.copy()

    for i in range(len(items)):
        for j in range(len(items) - i - 1):

            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items


def python_sort(items):
    return sorted(items)


sort_data = list(range(1000, 0, -1))

bubble_time = timeit.timeit(
    lambda: bubble_sort(sort_data),
    number=10
)

built_in_time = timeit.timeit(
    lambda: python_sort(sort_data),
    number=10
)

print("Bubble Sort Time:", bubble_time)
print("Python Sort Time:", built_in_time)