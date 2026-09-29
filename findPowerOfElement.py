# Method Implementation
def find_power(base, exponent):
    # Base case
    if exponent == 0:
        return 1

    # Recursive case
    half_power = find_power(base, exponent // 2)

    # Calculate square of the half power
    result = half_power * half_power

    # If exponent is odd, multiply by the base
    if exponent % 2 != 0:
        result *= base

    return result


# Driver Code
base = int(input("Enter the base value: "))
exponent = int(input("Enter the exponent value: "))

# Function Calling
result = find_power(base, exponent)

# Display the result
print("The power of the element is:", result)