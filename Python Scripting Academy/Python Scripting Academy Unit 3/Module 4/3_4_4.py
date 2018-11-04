%%writefile currency_converter.py
def USD2EUR(amount):
    """
    Convert amount from US Dollars to Euros.   
    Use 1 USD = 0.831467 EUR    
    args:
        amount: US dollar amount (float)        
    returns:
        value: the equivalent of amount in Euros (float)
    """
    #TODO: Your code goes here
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
    value = 0.831467 * amount
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
    value = 0.889358 * amount
    return value
def main():
    amount = float(input("Enter amount in USD: $"))   
    # In British Pounds
    gbp = USD2GBP(amount)   
    print("${:.2f} USD = {:.2f} GBP".format(amount, gbp))  
if __name__ == '__main__':
    main()

%%bash
pydoc currency_converter