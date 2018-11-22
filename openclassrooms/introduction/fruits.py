inventaire = [("pommes", 22),("melons", 4),("poires", 18),("fraises",76),("prunes",51)]
inventaire = [(j,i) for (i,j) in inventaire]
inventaire = [(i,j) for (i,j) in sorted(inventaire)]
inventaire = [(j,i) for (i,j) in inventaire]
inventaire.reverse()
print(inventaire)