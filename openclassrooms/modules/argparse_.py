import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", type = int, help="le nombre à mettre au carré")
parser.add_argument("-v", "--verbose", action="store_true", 
	help="augmente la verbosité")
args = parser.parse_args()
#print("Vous avez précisé X =", args.x)
x = args.x
retour = x ** 2
if args.verbose:
	print("{} ^ 2 = {}".format(x, retour))
else:
	print(retour)