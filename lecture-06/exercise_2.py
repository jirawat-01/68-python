inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]

def update_inventory(inventory, item_name, quantity_sold):
    for item in inventory:
        if item[0] == item_name:
            item[1] -= quantity_sold
            break

def calculate_total_value(inventory):
    total = 0
    for item in inventory:
        total += item[1] * item[2]
    return total

def find_most_expensive(inventory):
    max_price = 0
    max_item = ""
    for item in inventory:
        if item[2] > max_price:
            max_price = item[2]
            max_item = item[0]
    return max_item

def add_item(inventory, item_name, quantity, price):
    for item in inventory:
        if item[0] == item_name:
            item[1] = quantity
            item[2] = price
            return
    inventory.append([item_name, quantity, price])


update_inventory(inventory, "Banana", 20)

total_value = calculate_total_value(inventory)

print("Total inventory value: $", round(total_value, 2))

expensive_item = find_most_expensive(inventory)

print("Most expensive item:", expensive_item)

add_item(inventory, "Eggs", 30, 0.25)
add_item(inventory, "Eggs", 50, 0.30)

print("\nUpdated Inventory:")
for item in inventory:
    print(item)
