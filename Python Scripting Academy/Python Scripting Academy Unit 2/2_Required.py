# [x] create Element_Quiz
# [x] copy and paste in edX assignment page
def get_names():
    names = []
    print("list any 5 of the first 20 elements in the Period table")
    for a in range(0,5):
        name = input("Enter the name of an element: ")
        while name == "":
            name = input("Enter the name of an element: ")
        for b in names:
            if name != b:
                pass
            else:
                print(name,"was already entered")
                name = input("Enter the name of an element: ")
        names.append(name)
    return names

def check(names):
    count = 0
    correct = []
    incorrect = list(names)
    for a in range(0,len(names)):
        print(a)
        for b in element_list:
            print(b)
            if names[a] == b:
                count += 20
                correct.append(b)
                incorrect.remove(b)
    return str(count)+"% correct\nFound: "+' '.join(correct).title()+"\nNot Found: "+" ".join(incorrect).title()

!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements.txt
element = open('elements.txt','r')
element_lines = element.read()
element_list = element_lines.lower().split('\n')
element.close
print(element_list)
print(check(get_names()))