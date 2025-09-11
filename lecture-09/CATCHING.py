try:
    value = int(input("Enter anumber: "))
    result  = 10 / value
except ValueError:
    print("Invalid input ! please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Emd of program")
