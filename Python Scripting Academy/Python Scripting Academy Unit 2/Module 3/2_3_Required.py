# [x] create poem mixer
# [x] copy and paste in edX assignment page
def word_mixer(a):
    g = []
    if len(a) < 5:
        return "Sorry, your list is too short, we cannot mix it"
    else:
        while len(a) > 5:
            b = []
            c = a.pop(len(a)-4)
            b.append(c)
            d = a.pop(0)
            b.append(d)
            e = a.pop()
            b.append(e)
            f = " ".join(b)
            g.append(f)
        return  "\n".join(g)

def program_flow():
    poem = input("enter a saying or poem : ")
    words_list = poem.split(" ")
    for a in range(0,len(words_list)):
        if len(words_list[a]) <= 3:
            words_list[a] = words_list[a].lower()
        elif len(words_list[a]) >= 6:
            words_list[a] = words_list[a].upper()
        else:
            pass
    print(word_mixer(words_list))
    
program_flow()