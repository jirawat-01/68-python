keep_going = 'y'

while keep_going.lower() == 'y':
    sales = float(input('Enter the amount of sales: '))
    commission = sales * 2.5
    print(f'the commission is ${commission:.2f}')
    keep_going = input('Do you want to calculate another y/n :')