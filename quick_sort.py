# ============================================================
#                    QUICK SORT
#              Divide and Conquer Approach
# ============================================================


def quick_sort(arr):
    """Sort the array using the Quick Sort algorithm."""

    # Base case
    if len(arr) <= 1:
        return arr

    # Choose the last element as pivot
    pivot = arr[-1]

    # Elements smaller than or equal to pivot
    left = [x for x in arr[:-1] if x <= pivot]

    # Elements greater than pivot
    right = [x for x in arr[:-1] if x > pivot]

    # Recursively sort left and right parts
    return quick_sort(left) + [pivot] + quick_sort(right)


# ============================================================
#                       MAIN PROGRAM
# ============================================================

print("=" * 55)
print("                  QUICK SORT")
print("=" * 55)

# Take array input from user
arr = list(map(
    int,
    input("Enter array elements separated by space: ").split()
))

print("\nOriginal Array :", arr)

# Apply Quick Sort
sorted_arr = quick_sort(arr)

# Display sorted array
print("Sorted Array   :", sorted_arr)

print("=" * 55)