from random import randint

def romanWriting(number):
    m=int(number/1000)
    cm=int((number-m*1000)/900)
    d=int((number-m*1000-cm*900)/500)
    cd=int((number-m*1000-cm*900-d*500)/400)
    c=int((number-m*1000-cm*900-d*500-cd*400)/100)
    xc=int((number-m*1000-cm*900-d*500-cd*400-c*100)/90)
    l=int((number-m*1000-cm*900-d*500-cd*400-c*100-xc*90)/50)
    xl=int((number-m*1000-cm*900-d*500-cd*400-c*100-xc*90-l*50)/40)
    x=int((number-m*1000-cm*900-d*500-cd*400-c*100-xc*90-l*50-xl*40)/10)
    ix=int((number-m*1000-cm*900-d*500-cd*400-c*100-xc*90-l*50-xl*40-x*10)/9)
    v=int((number-m*1000-cm*900-d*500-cd*400-c*100-xc*90-l*50-xl*40-x*10-ix*9)/5)
    iv=int((number-m*1000-cm*900-d*500-cd*400-c*100-xc*90-l*50-xl*40-x*10-ix*9-v*5)/4)
    i=int(number-m*1000-cm*900-d*500-cd*400-c*100-xc*90-l*50-xl*40-x*10-ix*9-v*5-iv*4)
    romanNumber=[]
    for j in range(m):
        romanNumber.append("M")
    for j in range(cm):
        romanNumber.append("CM")
    for j in range(d):
        romanNumber.append("D")
    for j in range(cd):
        romanNumber.append("CD")
    for j in range(c):
        romanNumber.append("C")
    for j in range(xc):
        romanNumber.append("XC")
    for j in range(l):
        romanNumber.append("L")
    for j in range(xl):
        romanNumber.append("XL")
    for j in range(x):
        romanNumber.append("X")
    for j in range(ix):
        romanNumber.append("IX")
    for j in range(v):
        romanNumber.append("V")
    for j in range(iv):
        romanNumber.append("IV")
    for j in range(i):
        romanNumber.append("I")
    return romanNumber
number=int(input("Please enter a number between 1 and 3999 : "))
print("".join(romanWriting(number)))