annee=input("Entrez une année: ")
if int(annee)%4 == 0 and int(annee)%100 != 0:
 print("annee bissextile")
else:
 print("annee non bissextile")

