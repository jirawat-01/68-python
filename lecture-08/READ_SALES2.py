with open('sales.txt','r') as sales_file:
    total_sales = 0.0
    for line in sales_file:
        amount = float(line)
        total_sales += amount
        print(format(amount, '.2f'))

    print(f"totai sales:{total_sales:.2f}")