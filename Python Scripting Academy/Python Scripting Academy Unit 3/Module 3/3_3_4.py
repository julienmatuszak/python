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


