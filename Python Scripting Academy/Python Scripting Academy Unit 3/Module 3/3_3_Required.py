# [x] Use the `inventory` dictionary in a program that asks the user for a UPC number, description, unit price, 
# quantity in stock.
# If the item already exists in the inventory, the information is updated, 
# and your program should display a message that it is updating the entry.
# If the item does NOT exists in the inventory, a new dictionary entry is created, 
# and your program should display a message that it is creating a new entry.
# Use try/except in the program.
# test cases
# For an existing item
'''
Enter UPC number: 839529
Enter item description: TOMATOS 1LB
Enter unit price: 1.55
Enter item quantity: 21
Existing item, updating: ['TOMATOS 1LB', 1.29, 25]
  UPC   | Description       |  Unit Price  |  Quantity 
-------------------------------------------------------
839529  | TOMATOS 1LB       |         1.55 |      21.00
'''
# For a new item
'''
Enter UPC number: 29430
Enter item description: ORANGE 1LB
Enter unit price: 0.99
Enter item quantity: 40
New item, creating ORANGE 1LB
  UPC   | Description       |  Unit Price  |  Quantity 
-------------------------------------------------------
29430   | ORANGE 1LB        |         0.99 |      40.00
'''
inventory = {847502: ['APPLES 1LB', 1.99, 50], 847283: ['OLIVE OIL', 10.99, 100], 839529: ['TOMATOS 1LB', 1.29, 25], 483946: ['MILK 1/2G', 3.45, 35], 493402: ['FLOUR 5LB', 2.99, 40], 485034: ['BELL PEPPERS 1LB', 1.35, 28], 828391: ['WHITE TUNA', 1.69, 100], 449023: ['CHEESE 1/2LB', 4.99, 15]}
num = 0
description = ""
unit_price = 0
item_quantity = 0
while num == 0:
    try:
        num = int(input("Enter UPC number: "))
    except ValueError as exception:
        print(exception)
while description == "":
    description = input("Enter item description: ")          
while unit_price == 0:
    try:
        unit_price = float(input("Enter unit price: "))
    except ValueError as exception:
        print(exception)
while item_quantity == 0:
    try:
        item_quantity = float(input("Enter item quantity: "))
    except ValueError as exception:
        print(exception)
if num not in inventory.keys():
    print("New item, creating {:s}".format(description))
    inventory.update({num:[description, unit_price, item_quantity]})
if num in inventory.keys():
    print("Existing item, updating: {:s}".format(str(inventory[num])))
    inventory[num] = [description,unit_price,item_quantity]
print()
print("{:^9s}| {:<18s}|{:^13s}| {:^10s}".format("UPC","Description","Unit Price", "Quantity"))
print("-------------------------------------------------------")
print("{:<9d}| {:<18s}|{:>12.2f} |{:>11.2f}".format(num, inventory[num][0], inventory[num][1], inventory[num][2]))

# [x] Write a program to display the current inventory information as follow
# Note the items are sorted by UPC
'''
  UPC   | Description       |  Unit Price  |  Quantity 
-------------------------------------------------------
449023  | CHEESE 1/2LB      |         4.99 |      15.00
483946  | MILK 1/2G         |         3.45 |      35.00
485034  | BELL PEPPERS 1LB  |         1.35 |      28.00
493402  | FLOUR 5LB         |         2.99 |      40.00
828391  | WHITE TUNA        |         1.69 |     100.00
839529  | TOMATOS 1LB       |         1.29 |      25.00
847283  | OLIVE OIL         |        10.99 |     100.00
847502  | APPLES 1LB        |         1.99 |      50.00
'''
inventory = {847502: ['APPLES 1LB', 1.99, 50], 847283: ['OLIVE OIL', 10.99, 100], 839529: ['TOMATOS 1LB', 1.29, 25], 483946: ['MILK 1/2G', 3.45, 35], 493402: ['FLOUR 5LB', 2.99, 40], 485034: ['BELL PEPPERS 1LB', 1.35, 28], 828391: ['WHITE TUNA', 1.69, 100], 449023: ['CHEESE 1/2LB', 4.99, 15]}
print("{:^8s}| {:<18s}|{:^14s}|{:^12s}".format("UPC","Description","Unit Price","Quantity"))
print("-------------------------------------------------------")
for item in sorted(inventory.keys()):
    print("{:<8d}| {:<18s}|{:>13.2f} |{:>11.2f}".format(item, inventory[item][0], inventory[item][1], inventory[item][2]))