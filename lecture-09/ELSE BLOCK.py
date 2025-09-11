try:
    value = int(input("Enter anumber: "))
    result = 10 / value
except ZeroDivisionError:
    print("cannot divide by zero!")
else:
    print(f"the result is {result}")
print("End of program")
