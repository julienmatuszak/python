/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/

def proportion(sequence,chaine):
    i=0
    #i,j=0,0
    #for j in range(0,len(chaine)):
        #if sequence[j] == chaine
    for j in range(0,len(chaine)):
        if sequence[0] == chaine[j]:
            if sequence in chaine:
                i+=1
            continue
    pourcentage=float(100*i/len(chaine))
    print(pourcentage)
    print("Il y a {:.2f} % de \"{}\" dans votre chaine.".format(pourcentage,sequence))
    
def valide(chaine):
    for i in chaine:
        if i != 'a' and i!= 't' and i!= 'c' and i!='g':
            return False
    return True

def saisie():
    chaine = input("Saisissez une chaine ADN : ")
    if valide(chaine):
        print("Bravo! La chaine est valide.")
        sequence = input("Veuillez saisir une sequence ADN dont nous allons calculer la proportion dans la chaine : ")
        proportion(sequence,chaine)
    else:
        print("Vous n'avez pas effectue une bonne saisie. Veuillez recommencer.")
        saisie()
 
saisie()
