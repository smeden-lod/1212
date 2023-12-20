from chaine import Chaine

def appliquer(ch, f):
    """
    f: int -> int une fonction qui prend en entrée un int et renvoie un int
    ch: Chaine
    renvoie la chaine construite à partir des f(x) pour chaque x dans l
    """
    pass

def reduire(ch, f, acc) -> int:
    """
    f: (int, int) -> int en entrée un tuple de int renvoie un int
    acc: int
    ch: Chaine
    exemples: 
    reduire(ch, lambda x, y: x+y, 0) calcule la somme des valeurs dans ch
    reduire(ch, lambda x, y: x*y, 1) calcule le produit des valeurs dans ch
    """
    pass

def filtrer(ch, f):
    """
    f : int -> bool
    ch : Chaine
    renvoie la Chaine des valeurs x dans self telles que f(x) est True 
    exemple:
    filtrer(ch, lambda x: x<5) renvoie la chaine avec les valeurs dans ch qui sont <5 (dans le même ordre)
    """
    pass



