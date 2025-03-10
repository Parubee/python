try:
    value = int(input("Enter a number: "))
    result = 100 / value
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
