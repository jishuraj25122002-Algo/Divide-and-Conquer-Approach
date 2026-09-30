# Function to find the number of possible ways to climb n stairs
def possibilities(n):
    # Base cases
    if n == 0:
        return 1
    elif n == 1:
        return 1

    # Recursive case
    return possibilities(n - 1) + possibilities(n - 2)


# Driver Code
n = int(input("Enter the number of stairs: "))

if n < 0:
    print("Please enter a non-negative number.")
else:
    result = possibilities(n)
    print(f"Number of possible ways: {result}")