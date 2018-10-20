# [x] create, call and test the str_analysis() function  
# then PASTE THIS CODE into edX
def str_analysis(str):
    if str.isalpha():
        return "\""+str+"\""+" is all alphabetical characters!"
    elif str.isdigit():
        if int(str) < 100:
            return str+" is a smaller number than expected"
        else:
            return str+" is a pretty big number"
    else:
        return "Sorry, there is not much we can say about your string"

str = ""
while str == "":
    str = input("enter a word or integer : ")
print(str_analysis(str))

