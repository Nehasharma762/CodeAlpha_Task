"""FIBONACCI GENERATOR

The Fibonacci series is a sequence where each number is
the sum of the two preceding numbers, defined by a
mathematical recurrence relationship. """

def fibonacci(n):
    a, b = 0, 1  
    for _ in range(n):
        print(a, end=" ")  # Print the current number
        a, b = b, a + b  # Update to the next numbers

num_terms = int(input("Enter the number of terms: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci(num_terms)
