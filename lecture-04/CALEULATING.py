max = 5
total = 0.0

print('This program calculates the sum of')
print(max, 'numbers you will enter.')

for counter in range(max):
    number = int (input('Enrer a number:'))
    total = total + number

print('the total is ',total)