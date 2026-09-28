 # ============================================================
#                  INSERTION SORT
# ============================================================

def insertion_sort(arr):
    """
    Sorts a list of elements in ascending order
    using the Insertion Sort algorithm.
    """

    # Start from the second element
    for i in range(1, len(arr)):

        # Current element to be inserted
        key = arr[i]

        # Index of the previous element
        j = i - 1

        # Shift elements greater than key
        # one position to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key at its correct position
        arr[j + 1] = key

    return arr


# ============================================================
#                     DRIVER CODE
# ============================================================

# Read number of elements
n = int(input("Enter the number of elements: "))

# Read elements from the user
arr = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Sort the array
result = insertion_sort(arr)

# Display the sorted array
print("\nSorted Array:", result)