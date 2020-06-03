total_times_count = 0

def count_down(n):

    if n == 0:
        return

        count_down(n - 1)
        # count_down(n - 1)

# O(c^n)
# O(n)

#(2^5)
#(2^10)

count_down(5)
print(total_times_count)


def half(n):
    if n <= 1:

    half(n/2)

    # O(log n)