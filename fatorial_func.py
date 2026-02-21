def factorial(n):
    """Calculates the factorial of a number using recursion."""
    # Base case: if n is 1, the recursion stops and returns 1
    if n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n-1)

# Get integer input from the user
num=int(input("Enter a number : "))
# Call the function and store the result
fact=factorial(num)
# Display the final calculation
print(f"factorial of {num} is {fact}")
