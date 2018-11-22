from test2_classe import *

un_test = Test()

un_test.afficher_attribut()

print(dir(un_test))

print(un_test.__dict__)

un_test.__dict__["mon_attribut"] = "plus ok"

print(un_test.__dict__)

un_test.afficher_attribut()