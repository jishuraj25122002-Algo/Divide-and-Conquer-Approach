 # Method Implementation

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Driver code

arr = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    ele = int(input("Enter the element: "))
    arr.append(ele)

print("Before sorting the array is:", arr)

bubble_sort(arr)

print("After sorting the array is:", arr)