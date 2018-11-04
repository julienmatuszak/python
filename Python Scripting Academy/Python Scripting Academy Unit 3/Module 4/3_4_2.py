# [x] Fix the program below so it displays the area of a square with a side = 2
# Compute the area of a square
def square_area (side):
    # area is a local variable in square_area
    area = side ** 2
    return area
# Global scope
print(square_area(2))
# area is not within scope anymore and cannot be
# accessed from this global scope

# [x] Fix the program below so it displays the area of a square with side = 2
# and the volume of a cube with side = 2
# Compute the area of a square
def square_area (side):
    # area is a local variable in square_area
    area = side ** 2
    return area
# Compute the volume of a cube
def cube_volume (side):
    # cube volume = area of base X side
    volume = square_area(side) * side # area is not defined within this scope
    return volume
# Global scope
s = 2
square_area(s)
# area was deleted when the local scope of square_area was destroyed
cube_volume(s)

# [x] The program below converts US Dollars to Euros, British Pounds, and Japanese Yen
# Complete the functions USD2EUR, USD2GBP, USD2JPY so they all return the correct value
def USD2EUR(amount):
    """
    Convert amount from US Dollars to Euros.
    
    Use 1 USD = 0.831467 EUR
    
    args:
        amount: US dollar amount (float)        
    returns:
        value: the equivalent of amount in Euros (float)
    """
    value = 0.831467 * amount
    return value
def USD2GBP(amount):
    """
    Convert amount from US Dollars to British Pounds.    
    Use 1 USD = 0.739472 GBP    
    args:
        amount: US dollar amount (float)        
    returns:
        value: the equivalent of amount in British Pounds (float)
    """
    value = 0.739472 * amount
    return value
def USD2JPY(amount):
    """
    Convert amount from US Dollars to Japanese Yen.    
    Use 1 USD = 112.656 JPY    
    args:
        amount: US dollar amount (float)        
    returns:
        value: the equivalent of amount in Japanese Yen (float)
    """
    value = 112.656 * amount
    return value
def main():
    amount = float(input("Enter amount in USD: $"))    
    # In Euros
    eur = USD2EUR(amount)   
    # In British Pounds
    gbp = USD2GBP(amount)   
    # In Japanese Yen
    jpy = USD2JPY(amount)
    print("${:.2f} USD = {:.2f} EUR, {:.2f} GBP, {:.2f} JPY".format(amount, eur, gbp, jpy))    
if __name__ == '__main__':
    main()
    
# [x] The program below converts US Dollars to British Pounds. However, the conversion rate is unknown
# Complete the functions USD2EUR, EUR2GBP, and USD2GBP so they all return the correct value
# You should use USD2EUR and EUR2GBP in USD2GBP, do not try to find out the conversion rate
def USD2EUR(amount):
    """
    Convert amount from US Dollars to Euros.    
    Use 1 USD = 0.831467 EUR    
    args:
        amount: US dollar amount (float)
        
    returns:
        value: the equivalent of amount in Euros (float)
    """
    value = 0.831467 * amount
    return value
def EUR2GBP(amount):
    """
    Convert amount from Euros to British Pounds.    
    Use 1 EUR = 0.889358 GBP   
    args:
        amount: Euros amount (float)        
    returns:
        value: the equivalent of amount in GBP (float)
    """
    value = 0.889358 * amount
    return value
def USD2GBP(amount):
    """
    Convert amount from US Dollars to British Pounds.    
    The conversion rate is unknown, you have to use USD2EUR and EUR2GBP    
    args:
        amount: US dollar amount (float)
        
    returns:
        value: the equivalent of amount in British Pounds (float)
    """
    #TODO: Your code goes here
    value = EUR2GBP(USD2EUR(amount))
    return value
def main():
    amount = float(input("Enter amount in USD: $"))
    # In British Pounds
    gbp = USD2GBP(amount)
    print("${:.2f} USD = {:.2f} GBP".format(amount, gbp))
if __name__ == '__main__':
    main()

# [x] The following program converts an amount from US Dollars to Indian Rupees using the XCHANGE_RATE variable
# Complete the function USD2INR so it performs the conversion
XCHANGE_RATE = 63.6856 # = 1 USD
def USD2INR(amount):
    """
    Convert amount from US Dollars to Indian Rupees.   
    Use XCHANGE_RATE    
    args:
        amount: US dollar amount (float)       
    returns:
        value: the equivalent of amount in Indian Rupees (float)
    """
    value = XCHANGE_RATE*amount
    return value
print("Current exchange rate $1 USD = {} INR".format(XCHANGE_RATE))
amount = 220 #USD
inr = USD2INR(amount)
print("${} = {}".format(amount, inr))


