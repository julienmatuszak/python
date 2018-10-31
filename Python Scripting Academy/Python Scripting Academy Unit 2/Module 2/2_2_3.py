# [x] complete "replace items in a list" task
three_num = [1,9,0]
print(three_num)
if(three_num[0] < 5):
    three_num[0] = "small"
else:
    three_num[0] = "large"
print (three_num)

# [x]  create challenge function
def str_replace(int_list,index):
    while index < len(int_list):
        if(int_list[index] < 5):
            int_list[index] = "small"
        else:
            int_list[index] = "large"
        index += 1
    return(int_list)

int_list = [1,2,3,4,5,6,7,8,9]
index = 0
print(str_replace(int_list,index))

# [x] complete coding task described above
three_words = ["Hello", "World", "Julien"]
print(three_words)
three_words[0] = three_words[0].upper()
three_words[2] = three_words[2].swapcase()
print(three_words)

# [x] insert a name from user input into the party_list in the second position (index 1)
party_list = ["Joana", "Alton", "Tobias"]
party_list.insert(1,input("Add a new name for guest : "))
# [x] print the updated list
print(party_list)

# [x] Fix the Error
tree_list = ["oak"]
print("tree_list before =", tree_list)
tree_list.insert(1,"pine")
print("tree_list after  =", tree_list)
