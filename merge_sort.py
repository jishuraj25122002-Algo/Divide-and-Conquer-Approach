# ---------------------------------------------------------
# Merge Sort Implementation
# ---------------------------------------------------------

def merge_sort(arr, i, j):
    """Sort the array using the Merge Sort algorithm."""

    # Divide
    if i < j:
        # Find the middle index
        mid = i + (j - i) // 2

        # Conquer: sort the left half
        merge_sort(arr, i, mid)

        # Conquer: sort the right half
        merge_sort(arr, mid + 1, j)

        # Combine: merge both sorted halves
        merge_procedure(arr, i, mid, j)

    return arr


def merge_procedure(arr, i, mid, j):
    """Merge two sorted subarrays into one sorted subarray."""

    # Size of the two subarrays
    n1 = mid - i + 1
    n2 = j - mid

    # Create temporary arrays
    left_subarray = [0] * n1
    right_subarray = [0] * n2

    # Copy elements into the left subarray
    for m in range(n1):
        left_subarray[m] = arr[i + m]

    # Copy elements into the right subarray
    for n in range(n2):
        right_subarray[n] = arr[mid + 1 + n]

    # Initial indexes
    p = 0
    q = 0
    k = i

    # Merge the two subarrays
    while p < n1 and q < n2:

        if left_subarray[p] <= right_subarray[q]:
            arr[k] = left_subarray[p]
            p += 1
        else:
            arr[k] = right_subarray[q]
            q += 1

        k += 1

    # Copy remaining elements from the left subarray
    while p < n1:
        arr[k] = left_subarray[p]
        p += 1
        k += 1

    # Copy remaining elements from the right subarray
    while q < n2:
        arr[k] = right_subarray[q]
        q += 1
        k += 1


# ---------------------------------------------------------
# Driver Code
# ---------------------------------------------------------

arr = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Starting and ending indexes
i = 0
j = len(arr) - 1

# Display original array
print("\nOriginal array:", arr)

# Apply Merge Sort
result = merge_sort(arr, i, j)

# Display sorted array
print("Sorted array after applying Merge Sort:", result)