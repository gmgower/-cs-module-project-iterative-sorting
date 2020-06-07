def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found

    # other way


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low+high) // 2
        if target < arr[middle]:
            # eliminate RHS
            high = middle - 1
        elif target > arr[middle]:
            # eliminate LHS
            low = middle + 1
        else:
            return middle
    return -1  # not found


"""
def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    while low <= high:
        # go to the middle
        middle = (low + high)//2

    # ask if the middle is less than or greater than our target
    # if less, eliminate the right-hand side
    if target < arr[middle]:
        high = middle - 1

    elif target > arr[middle]:
        low = middle + 1

    else:
        return middle

        # adjust the low or high accordingly

    return -1  # not found
"""