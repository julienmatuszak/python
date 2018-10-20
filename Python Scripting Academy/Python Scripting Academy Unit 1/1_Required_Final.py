# [x] create, call and test the adding_report() function
# then PASTE THIS CODE into edX

def adding_report(report):
    total = 0
    items = ""
    print('Input an integer to add to the total or "Q" to quit')
    while True:
        item = input('Enter an integer or "Q" : ')
        if item.upper().startswith("Q"):
            if report.upper() =="A":
                print("\nItems"+items)
            print("\nTotal\n",total)
            break
        elif item.isdigit() is False:
            print(item," is invalid input")
        else:
            total += int(item)
            if report.upper() == "A":
                items += "\n"+item

report = "T"
all_report = input("Would you like a report for all operations (yes/no) ? ")
if all_report.lower().startswith("y"):
    report = "A"
else:
    pass
adding_report(report)