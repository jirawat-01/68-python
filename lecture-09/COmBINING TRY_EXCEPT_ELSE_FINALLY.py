try:
    value = int(input("Enter a number:"))
    result = 10 / value

except ValueError:
    print("Invaild input! please enter a number.")
except ZeroDivisionError:
    print(f"Cannot divide by zero!")
else:
    print(f"the result is {result}")
finally:
    print("Exception completed.")
    