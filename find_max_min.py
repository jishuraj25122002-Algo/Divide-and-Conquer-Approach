# ============================================================
#        FIND MAXIMUM AND MINIMUM USING DIVIDE AND CONQUER
# ============================================================


def find_max_min(arr, low, high):
    """
    Finds the maximum and minimum values in an array
    using the Divide and Conquer approach.

    Parameters:
        arr  : List of elements
        low  : Starting index
        high : Ending index

    Returns:
        (maximum, minimum)
    """

    # --------------------------------------------------------
    # Base Case 1: Only one element
    # --------------------------------------------------------
    if low == high:
        return arr[low], arr[low]

    # --------------------------------------------------------
    # Base Case 2: Two elements
    # --------------------------------------------------------
    if high == low + 1:

        if arr[low] > arr[high]:
            return arr[low], arr[high]

        return arr[high], arr[low]

    # --------------------------------------------------------
    # Divide: Find the middle index
    # --------------------------------------------------------
    mid = low + (high - low) // 2

    # --------------------------------------------------------
    # Conquer: Find max and min in both halves
    # --------------------------------------------------------
    max_left, min_left = find_max_min(arr, low, mid)
    max_right, min_right = find_max_min(arr, mid + 1, high)

    # --------------------------------------------------------
    # Combine: Compare results from both halves
    # --------------------------------------------------------
    maximum = max(max_left, max_right)
    minimum = min(min_left, min_right)

    return maximum, minimum


# ============================================================
#                     DRIVER CODE
# ============================================================

# Read the number of elements
n = int(input("Enter the number of elements: "))

# Read array elements
arr = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)


# ------------------------------------------------------------
# Define the starting and ending indices
# ------------------------------------------------------------

low = 0
high = len(arr) - 1


# ------------------------------------------------------------
# Function call
# ------------------------------------------------------------

max_value, min_value = find_max_min(arr, low, high)


# ------------------------------------------------------------
# Display the result
# ------------------------------------------------------------

print("\n" + "=" * 50)
print("              ARRAY RESULTS")
print("=" * 50)

print(f"Array   : {arr}")
print(f"Maximum : {max_value}")
print(f"Minimum : {min_value}")

print("=" * 50)
