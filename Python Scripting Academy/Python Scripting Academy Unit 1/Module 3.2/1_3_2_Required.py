# [x] create, call and test 
# then PASTE THIS CODE into edX

def cheese_order():
    max_weight = 100
    min_weight = 1
    price_kilo = 7.99
    order = float(input("Enter cheese order weight (numeric value): "))
    if (order > max_weight):
        print(order,"is more than currently available stock")
    elif (order < min_weight):
        print(order,"is below minimum order amount")
    else:
        print(order,"costs $"+str(order*price_kilo))

    
cheese_order()
cheese_order()
cheese_order()
