# [x] create, call and test fishstore() function 
def fishstore(fish,price):
    rtn = "Fish Type: "+ fish + " costs " + price
    return(rtn)

fish_entry = input("What is the name of the fish ? ")
price_entry = input("What is the price of the fish ? ")
print(fishstore(fish_entry,price_entry))
# then PASTE THIS CODE into edX