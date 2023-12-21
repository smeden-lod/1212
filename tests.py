from chaine import *

l = Chaine(11, Chaine(3, Chaine(5, ChaineVide())))

assert l.take(1) == Chaine(11, ChaineVide())
print("test OK")
