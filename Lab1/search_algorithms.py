# Lab 1: Search Algorithms
# This file covers linear search and array comparison algorithms

print("=" * 60)
print("LINEAR SEARCH")
print("=" * 60)


def linear_search(items, target):
    """Return the index of target in items, or -1 if not found."""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


numbers = [10, 23, 45, 70, 11, 15, 20]
print("List:", numbers)

# Value that exists
target = 45
index = linear_search(numbers, target)
if index != -1:
    print(f"{target} found at index {index}")
else:
    print(f"{target} not found")

# Value that does not exist
target = 99
index = linear_search(numbers, target)
if index != -1:
    print(f"{target} found at index {index}")
else:
    print(f"{target} not found")

print("\n" + "=" * 60)
print("FIND IN TWO ARRAYS")
print("=" * 60)


def find_in_two_arrays(first, second, target):
    """Return a message describing where target appears in the arrays."""
    first_index = -1
    second_index = -1

    for i in range(len(first)):
        if first[i] == target:
            first_index = i

    for i in range(len(second)):
        if second[i] == target:
            second_index = i

    if first_index != -1 and second_index != -1:
        return (f"{target} found in both arrays "
                f"(index {first_index} and {second_index})")
    elif first_index != -1:
        return f"{target} found only in the first array at index {first_index}"
    elif second_index != -1:
        return (f"{target} found only in the second array "
                f"at index {second_index}")
    else:
        return f"{target} not found in either array"


array_a = [3, 7, 12, 25, 42]
array_b = [8, 12, 25, 50, 77]

print("Array A:", array_a)
print("Array B:", array_b)
print()

print(find_in_two_arrays(array_a, array_b, 25))
print(find_in_two_arrays(array_a, array_b, 3))
print(find_in_two_arrays(array_a, array_b, 8))
print(find_in_two_arrays(array_a, array_b, 99))

print("\n" + "=" * 60)
print("COMMON ELEMENTS IN TWO ARRAYS")
print("=" * 60)


def common_elements(first, second):
    """Return the list of values present in both arrays."""
    common = []
    for value in first:
        if value in second and value not in common:
            common.append(value)
    return common


array_a = [1, 2, 3, 4, 5]
array_b = [4, 5, 6, 7, 8]

print("Array A:", array_a)
print("Array B:", array_b)
print("Common elements:", common_elements(array_a, array_b))
