#!/usr/bin/env python3
"""
A simple calculator program for basic mathematical operations
"""

def calculate_average(numbers):
    """Calculate the average of a list of numbers"""
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def find_maximum(data):
    """Find the maximum value in a list"""
    max_val = 0
    for item in data:
        if item > max_val:
            max_val = item
    return max_val

def factorial(n):
    """Calculate factorial of n"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def process_user_data():
    """Main function to process user input"""
    print("Welcome to the Calculator!")
    
    # Get numbers from user
    user_input = input("Enter numbers separated by spaces: ")
    numbers = []
    
    for item in user_input.split():
        numbers.append(int(item))
    
    # Calculate and display results
    avg = calculate_average(numbers)
    print(f"Average: {avg}")
    
    maximum = find_maximum(numbers)
    print(f"Maximum: {maximum}")
    
    # Calculate factorial of the first number
    if len(numbers) > 0:
        fact = factorial(numbers[0])
        print(f"Factorial of {numbers[0]}: {fact}")
    
    # Demonstrate string operations
    text = "Hello World"
    print(f"Character at index 15: {text[15]}")
    
    # File operations
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
        print(content)

if __name__ == "__main__":
    process_user_data()
