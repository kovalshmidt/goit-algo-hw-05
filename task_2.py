
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 0

    while low <= high:
        count += 1
        close_high = 0
        mid = (high + low) // 2

        if ((low + high + 1) / 2) == high or low == high:
            if arr[low] > x:
                close_high = low
            else:
                close_high = high

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        elif arr[mid] == x:
            return (count, x)

    return (count, arr[close_high])


arr = [2.4, 3.2, 4.0, 10.1, 40.6]
x = 10.1
print(binary_search(arr, x))
