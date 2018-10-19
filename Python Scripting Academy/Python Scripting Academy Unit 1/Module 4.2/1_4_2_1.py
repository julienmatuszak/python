# [x] create Get Name program
familiar_name = ""
while True:
    familiar_name = input("common name friends / family use: ")
    if familiar_name.isalpha() is False:
        print("Sorry, you entered a wrong name (no space, characters or digits)")
    else:
        break
        
print("Hello "+familiar_name+"!")

# [x] Create the Shirt Count program, run tests
shirt_count = 0
count_S = 0
count_M = 0
count_L = 0
while True:
    size = input("Welcome to my shop ! Enter the size of the shirt you wanna buy (S / M / L / exit when finished) : ")
    if size == "exit":
        break
    shirt_count += 1
    if size.upper().startswith("S"):
        count_S +=1
    if size.upper().startswith("M"):
        count_M +=1
    if size.upper().startswith("L"):
        count_L +=1
    
print("Number of shirts bought : ",shirt_count," -> ",count_S,"size S, ",count_M,"size M, ",count_L,"size L")

# [x] Create the Shirt Register program, run tests
shirt_count = 0
count_S = 0
count_M = 0
count_L = 0
total = 0
total_S = 0
total_M = 0
total_L = 0
while True:
    size = input("Welcome to my shop ! Enter the size of the shirt you wanna buy (S / M / L / exit when finished) : ")
    if size == "exit":
        break
    shirt_count += 1
    if size.upper().startswith("S"):
        count_S +=1
        total += 6
        total_S += 6
    if size.upper().startswith("M"):
        count_M +=1
        total += 7
        total_M += 7
    if size.upper().startswith("L"):
        count_L +=1
        total += 8
        total_L += 8
        
print("Number of shirts bought : ",shirt_count," ->",count_S,"for size S, ",count_M,"for size M, ",count_L,"for size L")
print("Total: $"+str(total),":",str(total_S),"for size S,",str(total_M),"for size M,",str(total_L),"for size L")
