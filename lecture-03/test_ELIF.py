num_employees = int(input("enter the number of employees : "))
if num_employees < 50:
    print("This is a small company.")
elif num_employees < 250:
    print("This is a medium-sized company.")
elif num_employees > 250:
    print("The is a large company.")