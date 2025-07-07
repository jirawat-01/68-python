hours_worked = int(input("Enter the number of hours worked: "))
hourly_rate = int(input("Enter the hourly pay rate : "))
if hours_worked <= 40:
    gross_pay = hours_worked * hourly_rate
else:
    regular_pay = 40 * hourly_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * hourly_rate * 1.5
    gross_pay = regular_pay + overtime_pay

print(f"The gross pay is ${gross_pay:.2f}")
