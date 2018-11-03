# [x] The `data` list contains information about a company's employees.
# Use the `data` list and an appropriate loop to create a dictionary of employees.
# Use IDs (as keys) and names (as values).
# Ignore the email addresses for now.
# The created dictionary should look like:
# {57394: 'Suresh Datta', 48539: 'Colette Browning', 58302: 'Skye Homsi', 48502: 'Hiroto Yamaguchi', 48291: 'Tobias Ledford', 48293: 'Jin Xu', 23945: 'Joana Dias', 85823: 'Alton Derosa'}
data = [["Suresh Datta", 57394, "suresh@example.com"], ["Colette Browning", 48539, "colette@example.com"], ["Skye Homsi", 58302, "skye@example.com"], ["Hiroto Yamaguchi", 48502, "hiroto@example.com"], ["Tobias Ledford", 48291, "tobias@example.com", "Tamara Babic", 58201, "tamara@example.com"], ["Jin Xu", 48293, "jin@example.com"], ["Joana Dias", 23945, "joana@example.com"], ["Alton Derosa", 85823, "alton@example.com"]]
dictionary = {}
for a in data:
    dictionary[a[1]] =a[0]
print (dictionary)

# [x] Use the `records` dictionary in a program that asks the user for an ID and prints the name of the associated employee.
# Display an appropriate message if the ID is not found in the dictionary.
records = {57394: 'Suresh Datta', 48539: 'Colette Browning', 58302: 'Skye Homsi', 48502: 'Hiroto Yamaguchi', 48291: 'Tobias Ledford', 48293: 'Jin Xu', 23945: 'Joana Dias', 85823: 'Alton Derosa'}
# Ask user for a name, then display the number
number = int(input("Enter the ID of the user : "))
# If name is not in the contacts dictionary, the exception message will be displayed
try:
    name = records[number]
    print("Name is: {:s}".format(name))
except KeyError as exception_object:
    print("{:d} was not found in contacts".format(number))

# [x] Use the `records` dictionary in a program to ask the user for an ID then delete the employee record associated with the ID
# The program should display an appropriate message if the ID is not found in the dictionary.
records = {57394: 'Suresh Datta', 48539: 'Colette Browning', 58302: 'Skye Homsi', 48502: 'Hiroto Yamaguchi', 48291: 'Tobias Ledford', 48293: 'Jin Xu', 23945: 'Joana Dias', 85823: 'Alton Derosa'}
number = int(input("Enter a number : "))
try:
    name = records.pop(number)
    print("{:s}: {:d} was deleted from contacts".format(name, number))
except KeyError as exception_object:
    print("{:s} was not found in contacts".format(name))
print("Updated contact:", records)

# [x] The `data` list contains information about a company's employees
# Use the `data` list and an appropriate loop to create a dictionary of
# IDs (as keys): [name, email] (as values)
# The resulting dictionary should look like: 
# {57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com'], 48502: ['Hiroto Yamaguchi', 'hiroto@example.com'], 48291: ['Tobias Ledford', 'tobias@example.com'], 48293: ['Jin Xu', 'jin@example.com'], 23945: ['Joana Dias', 'joana@example.com'], 85823: ['Alton Derosa', 'alton@example.com']}
data = [["Suresh Datta", 57394, "suresh@example.com"], ["Colette Browning", 48539, "colette@example.com"], ["Skye Homsi", 58302, "skye@example.com"], ["Hiroto Yamaguchi", 48502, "hiroto@example.com"], ["Tobias Ledford", 48291, "tobias@example.com", "Tamara Babic", 58201, "tamara@example.com"], ["Jin Xu", 48293, "jin@example.com"], ["Joana Dias", 23945, "joana@example.com"], ["Alton Derosa", 85823, "alton@example.com"]]
dictionary = {}
for a in data:
    dictionary[a[1]] = [a[0],a[2]]
print (dictionary)

# [x] Write a program to display the content of the `records` dictionary as shown here
# Note the IDs are sorted in an ascending order
'''
        Name         |     ID     |        Email        
________________________________________________________
     Joana Dias      |   23945    |    joana@example.com
   Tobias Ledford    |   48291    |   tobias@example.com
       Jin Xu        |   48293    |      jin@example.com
  Hiroto Yamaguchi   |   48502    |   hiroto@example.com
  Colette Browning   |   48539    |  colette@example.com
    Suresh Datta     |   57394    |   suresh@example.com
     Skye Homsi      |   58302    |     skye@example.com
    Alton Derosa     |   85823    |    alton@example.com
'''
records = {57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com'], 48502: ['Hiroto Yamaguchi', 'hiroto@example.com'], 48291: ['Tobias Ledford', 'tobias@example.com'], 48293: ['Jin Xu', 'jin@example.com'], 23945: ['Joana Dias', 'joana@example.com'], 85823: ['Alton Derosa', 'alton@example.com']}
print("{:^20s}|{:^14s}|{:^20s}".format("Name","ID","Email"))
print("________________________________________________________")
for item in sorted(records.keys()):
    print("{:^20s}|{:^14d}|{:>20s}".format(records[item][0], item, records[item][1]))

# [x] The company's domain has changed from (example.com) to (example.org)
# Write a program to modify the email addresses in the `records` dictionary to reflect this change
records = {57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com'], 48502: ['Hiroto Yamaguchi', 'hiroto@example.com'], 48291: ['Tobias Ledford', 'tobias@example.com'], 48293: ['Jin Xu', 'jin@example.com'], 23945: ['Joana Dias', 'joana@example.com'], 85823: ['Alton Derosa', 'alton@example.com']}
for item in sorted(records.keys()):
    records[item][1] = records[item][1].replace("com","org")
print("{:^20s}|{:^14s}|{:^20s}".format("Name","ID","Email"))
print("________________________________________________________")
for item in sorted(records.keys()):
    print("{:^20s}|{:^14d}|{:>20s}".format(records[item][0], item, records[item][1]))

# [x] You want to send a mass email to all company employees, so you need a list of all the email addresses in `records`
# Write a program to extract the email addresses from the `records` dictionary and store them in a list
# The output list should look like:
# ['suresh@example.com', 'colette@example.com', 'skye@example.com', 'hiroto@example.com', 'tobias@example.com', 'jin@example.com', 'joana@example.com', 'alton@example.com']
# Hint: use the `.values()` method
records = {57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com'], 48502: ['Hiroto Yamaguchi', 'hiroto@example.com'], 48291: ['Tobias Ledford', 'tobias@example.com'], 48293: ['Jin Xu', 'jin@example.com'], 23945: ['Joana Dias', 'joana@example.com'], 85823: ['Alton Derosa', 'alton@example.com']}
emails = []
for a in records.values():
    emails.append(a[1])
print (emails)

# Write a program that can ONLY update the price of an existing grocery 
# in the `groceries` dictionary.
# The item and updated price should be entered by the user.
# If the user enters a new item, the program should not create 
# a new dictionary item. It should instead display an error message.
groceries = {'Bread':2.26, 'Milk':3.62, 'Chocolate':1.59}
item = input("Enter the name of the item you want to change : ")
if item not in groceries:
    print("Price not in the dictionary")
elif (item in groceries):
    new_price = int(input("Enter the new price for this item : "))
    groceries[item] = new_price
print(groceries)

# [x] Write a program to find out the number of employees stored in `records`.
records = {57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com'], 48502: ['Hiroto Yamaguchi', 'hiroto@example.com'], 48291: ['Tobias Ledford', 'tobias@example.com'], 48293: ['Jin Xu', 'jin@example.com'], 23945: ['Joana Dias', 'joana@example.com'], 85823: ['Alton Derosa', 'alton@example.com']}
count = 0
for a in records.values():
    count +=1
print(count)
print(len(records))


