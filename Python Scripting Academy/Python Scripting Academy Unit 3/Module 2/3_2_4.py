# [x] Use the variables `F` and `C` to generate the following print outputs
'''
75 Fahrenheit = 23.888900 Celsius
75 Fahrenheit = 23.89 Celsius
75 Fahrenheit = 000023.889 Celsius
75 Fahrenheit = 23.889     Celsius
75 Fahrenheit =     23.889 Celsius
75 Fahrenheit = 2.389E+01 Celsius
75 Fahrenheit = 2.389e+01 Celsius
'''
F = 75
C = 23.8889
print("%d Fahrenheit = %f Celsius" % (F, C))
print("%d Fahrenheit = %.2f Celsius" % (F, C))
print("%d Fahrenheit = %5.3f Celsius" % (F, C))
print("%d Fahrenheit = %010.3F Celsius" % (F, C))
print("%d Fahrenheit = %10.3f Celsius" % (F, C))
print("%d Fahrenheit = %.3E Celsius" % (F, C))
print("%d Fahrenheit = %.3e Celsius" % (F, C))

# [x] Use the string variables below to generate the following print outputs
# HINT: Set the name formatter width to 10 characters
first_name = 'Tamara'
last_name = 'Babic'
'''
Name: Tamara Babic
Name:     Tamara      Babic
Name: Tamara          Babic
Name:     Tamara Babic     
Name: Tamara     Babic     
Name: Tamara Babic
'''   
print("Name: %s %s" % (first_name, last_name))
print("Name: %10s %10s" % (first_name, last_name))
print("Name: %s %14s" % (first_name, last_name))
print("Name: %10s %s" % (first_name, last_name))
print("Name: %s %9s" % (first_name, last_name))
print("Name: %s %s" % (first_name, last_name))

# [x] The list `data` contains personnel information (Name, ID, email)
# Write a program to print out the data as follows:
'''
Name                 ID         Email               
--------------------------------------------------
Suresh Datta         57394      suresh@example.com  
Colette Browning     48539      colette@example.com 
Skye Homsi           58302      skye@example.com    
Hiroto Yamaguchi     48502      hiroto@example.com  
Tobias Ledford       48291      tobias@example.com  
Jin Xu               48293      jin@example.com     
Joana Dias           23945      joana@example.com   
Alton Derosa         85823      alton@example.com 
'''
data = [["Suresh Datta", 57394, "suresh@example.com"], ["Colette Browning", 48539, "colette@example.com"], ["Skye Homsi", 58302, "skye@example.com"], ["Hiroto Yamaguchi", 48502, "hiroto@example.com"], ["Tobias Ledford", 48291, "tobias@example.com", "Tamara Babic", 58201, "tamara@example.com"], ["Jin Xu", 48293, "jin@example.com"], ["Joana Dias", 23945, "joana@example.com"], ["Alton Derosa", 85823, "alton@example.com"]]
print("Name                 ID         Email")
for a in range(50):
    print("-", end = "")
print("\n")
for a in data:
    print("%s" %a[0], end = "")
    print((21-len(a[0]))*" ", end = "")
    print("%s" %a[1], end = "")
    print("\t", end = "")
    print("%s" %a[2])

# [ ] Use Python-style formatting and the variables `F` and `C` to generate the following print outputs
'''
75 Fahrenheit = 23.888900 Celsius
75 Fahrenheit = 23.89 Celsius
75 Fahrenheit = 0000023.89 Celsius
75 Fahrenheit = 23.889     Celsius
75 Fahrenheit =   23.889   Celsius
75 Fahrenheit =     23.889 Celsius
75 Fahrenheit = 2.389E+01 Celsius
'''
F = 75
C = 23.8889
print("{:d} Fahrenheit = {:f} Celsius".format(F, C))
print("{:d} Fahrenheit = {:.2f} Celsius".format(F, C))
print("{:d} Fahrenheit = {:0>10.2f} Celsius".format(F, C))
print("{:d} Fahrenheit = {:<10.3F} Celsius".format(F, C))
print("{:d} Fahrenheit = {:8.3f} Celsius".format(F, C))
print("{:d} Fahrenheit = {:>10.3f} Celsius".format(F, C))
print("{:d} Fahrenheit = {:.3E} Celsius".format(F, C))

# [x] Use Python-style formatting and the string variables below to generate the following print outputs
# HINT: Set the name formatter width to 10 characters
first_name = 'Tamara'
last_name = 'Babic'
'''
Name: Tamara Babic
Name: Tamara          Babic
Name: Tamara____ _____Babic
Name: __Tamara__ __Babic___
Name: ____Tamara Babic_____
Name:     Tamara Babic     
'''   
print("Name: {:s} {:s}".format(first_name, last_name))
print("Name: {:10s} {:>10s}".format(first_name, last_name))
print("Name: {:_<10s} {:_>10s}".format(first_name, last_name))
print("Name: {:_^10s} {:_^10s}".format(first_name, last_name))
print("Name: {:_>10s} {:_<10s}".format(first_name, last_name))
print("Name: {: >10s} {: <10s}".format(first_name, last_name))

# [x] The list `data` contains personnel information (Name, ID, email)
# Write a program using Python-style formatting to print out the data as follows:
'''
        Name         |     ID     |        Email        
________________________________________________________
    Suresh Datta     |   57394    |   suresh@example.com
  Colette Browning   |   48539    |  colette@example.com
     Skye Homsi      |   58302    |     skye@example.com
  Hiroto Yamaguchi   |   48502    |   hiroto@example.com
   Tobias Ledford    |   48291    |   tobias@example.com
       Jin Xu        |   48293    |      jin@example.com
     Joana Dias      |   23945    |    joana@example.com
    Alton Derosa     |   85823    |    alton@example.com
'''
data = [["Suresh Datta", 57394, "suresh@example.com"], ["Colette Browning", 48539, "colette@example.com"], ["Skye Homsi", 58302, "skye@example.com"], ["Hiroto Yamaguchi", 48502, "hiroto@example.com"], ["Tobias Ledford", 48291, "tobias@example.com", "Tamara Babic", 58201, "tamara@example.com"], ["Jin Xu", 48293, "jin@example.com"], ["Joana Dias", 23945, "joana@example.com"], ["Alton Derosa", 85823, "alton@example.com"]]
print("        Name         |     ID     |        Email")
for a in range(55):
    print("_", end ="")
print(" \n")
for a in data:
    print("{:^21s}".format(a[0]), end = "")
    print("|", end ="")
    print("{:^12s}".format(str(a[1])), end = "")
    print("|", end ="")
    print("{:>20s}".format(a[2]))
