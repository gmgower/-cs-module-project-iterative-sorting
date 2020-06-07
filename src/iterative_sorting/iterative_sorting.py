# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # traverse loop through n-1 elements
    for i in range(0, len(arr) - 1): # loop until the second last el, range stops before last el.
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)): # inner loop will go to the last el
            # compare all these value to the value a cur_index
            # find the samllest
            if(arr[j] < arr[smallest_index]):
                smallest_index = j

        # TO-DO: swap
        # Your code here
        # https://youtu.be/-RfySCpOeV8?t=1170
        # arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        # a, b = (1, 2)
        # a == 1
        # b == 2
        # or
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr
    # O(n^2)

    # selection sort
    # [4, 6, 2, 3, 7, 1] # find smallest move to far left
    # [1, 4, 6, 2, 3, 7]
    # [1, 2, 4, 6, 3, 7]
    # [1, 2, 3, 4, 6, 7]
    # [1, 2, 3, 4, 6, 7]




# TO-DO:  implement the Bubble Sort function below
# def bubble_sort(arr):
#     # Your code here
#     for i in range(len(arr) - 1):
#         flag = 0
#         for i in range(len(arr) - 1):
#             if arr[i] > arr[i + 1]:
#                 temp = arr[i]
#                 arr[i] = arr[i + 1]
#                 arr[i + 1] = temp
#                 flag = 1

#         if flag == 0:
#             break

#     return arr

    # other way
def bubble_sort(arr):
    made_a_swap = True
    
    while made_a_swap:
        made_a_swap = False

        for i in range(0, len(arr) - 1):
            j = i + 1

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                made_a_swap = True
        
    return arr
# https://youtu.be/-RfySCpOeV8?t=1992
    #  i  j
    # [4, 3, 5, 7, 1]


# another way
# # TO-DO:  implement the Bubble Sort function below
# def bubble_sort(arr):
#     # Set incoming array to a variable for DRY code
#     init = range(len(arr) - 1)
#     # Tells second loop where to start at, runs for each value in the list
#     for i in init:
#         # Starts at 0
#         for j in init:
#             # Compare values
#             if arr[j] > arr[j+1]:
#                 # Perform the swap
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
# https: // youtu.be/-RfySCpOeV8?t = 1992
#   j
#   i
#  [2, 3, 1, 5]
'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
# count_sort is O(n)
"""
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return arr
​
   if maximum == -1:
        maximum = max(arr)
​
   counts = [0] * (maximum + 1)
​
   for value in arr:
        if value < 0:
            return "Error, negative numbers not allowed in Count Sort"
        counts[value] += 1

    j = 0
    for i in range(0, len(counts)):
        while counts[i] > 0:
            arr[j] = i
            j += 1
            counts[i] -= 1
​
    return arr
"""
# https: // youtu.be/-RfySCpOeV8?t = 2521

# array_to_be_sorted = [2,3,4,5,1]

# counts = [0, 0, 0, 0, 0, 0] #* (5 + 1)
# counts = [0, 0, 1, 0, 0, 0] # 2 indexes
# counts = [0, 0, 1, 1, 0, 0] # 3
# counts = [0, 0, 1, 1, 1, 0] # 4
# counts = [0, 0, 1, 1, 1, 1] # 5
# counts = [0, 1, 1, 1, 1, 1] # 1

# sorted_arry = [None, None, None, None, None] # index 1
# sorted_arry = [1, 2, 3, 4, 5]









# array_to_be_sorted
