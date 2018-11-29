mot = input("Entrez votre nom : ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
somme = 0

for a in mot:
	if a.lower() in alphabet:
		somme += alphabet.index(a.lower())
		somme += 1

print("Votre nom chiffré est maintenant :",str(somme))