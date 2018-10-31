# [x] create list-o-matic
# [x] copy and paste in edX assignment page
def build_list():
    liste = []
    item = ""
    while item.lower() != "quit":
        item = input("Please add some animal to the list (Quit to exit) : ")
        liste.append(item)
    liste.pop()
    return liste

def listomatic():
    liste = build_list()
    while liste != []:
        print("look at all the animals",liste)
        animal = input("enter the name of an animal: ")
        if animal == "":
            animal = liste.pop()
            print(animal+" popped from list\n")
        elif animal in liste:
            animal_deleted = animal
            liste.remove(animal)
            print("1 instance of",animal_deleted,"removed from list\n")
        else:
            animal_added = animal
            liste.append(animal)
            print("1 instance of",animal_added,"appended to list\n")
    print("Goodbye!")
    
print(listomatic())