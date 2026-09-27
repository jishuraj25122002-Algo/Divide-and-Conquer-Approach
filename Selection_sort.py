# ============================================
#        SELECTION SORT - PYTHON
# ============================================

def selection_sort(arr):
    """
    Sorts a list of elements in ascending order
    using the Selection Sort algorithm.
    """

    n = len(arr)

    # Move the boundary of the unsorted portion
    for i in range(n - 1):

        # Assume the first element is the minimum
        min_index = i

        # Find the smallest element in the remaining list
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first
        # element of the unsorted portion
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# ============================================
#              DRIVER CODE
# ============================================

arr = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Apply Selection Sort
result = selection_sort(arr)

# Display the result
print("\nOriginal/Entered Array :", arr)
print("Sorted Array            :", result) 