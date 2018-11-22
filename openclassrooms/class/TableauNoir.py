from TableauNoir_classe import *

tab = TableauNoir()

print(tab)
print(tab.surface)

tab.ecrire("Cool!")

print(tab.surface)

tab.ecrire("Cool mec!")

print(tab.surface)

print(tab.ecrire)
print(TableauNoir.ecrire)
#print(help(TableauNoir.__init__))

TableauNoir.ecrire(tab, 'essai')
print(tab.surface)
