from chaine import Chaine

def appliquer(self, f):
    """
    f: int -> int une fonction qui prend en entrée un int et renvoie un int
    self: Chaine
    renvoie la chaine construite à partir des f(x) pour chaque x dans l
    """
    pass

def reduire(self, f, acc) -> int:
    """
    f: (int, int) -> int en entrée un tuple de int renvoie un int
    acc: int
    self: Chaine
    exemples: 
    ch.reduire(lambda x, y: x+y, 0) calcule la somme des valeurs dans ch
    ch.reduire(lambda x, y: x*y, 1) calcule le produit des valeurs dans ch
    """
    pass

def filtrer(f, ch):
    """
    f : int -> bool
    self : Chaine
    renvoie la Chaine des valeurs x dans self telles que f(x) est True 
    """
    pass



