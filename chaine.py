"""
implémentations des listes chaînées
"""
from __future__ import annotations

class ChaineVide:
    
    def tete(self):
        raise ValueError("chaine vide")
    
    def queue(self):
        raise ValueError("chaine vide")


    def est_vide(self) -> bool:
        return True

    def __repr__(self) -> str:
        return "()"

    def longueur(self) -> int:
        return 0

    def contient(self, x: int) -> bool:
        return False

    def maxi(self):
        return float('-inf')


    def cons(self, v):
        """
        renvoi la chaine "ch" tel que :
        ch.tete() -> v
        ch.queue() -> self
        """
        return Chaine(v, self)

    def append(self, m: Chaine) -> Chaine:

        return Chaine(self, m)
        return Chaine(self, m)
    
    def append_iter(self, m) -> None:
        self = m

    def reverse(self) -> Chaine:
        return self

    def zip(self, other: Chaine, res:ChaineVide|Chaine) -> Chaine:
        """
        ## Input
        - other: Chaine à zipper avec self
        ## Output 
        - Chaine de tuple contenant forcement 2 variables venant chacun de self et res
        """
        return res

    def take(self, n) -> Chaine:
        """
        """
        return 0 

    def drop(self, n: int) -> Chaine:
        """
        """
        pass


class Chaine:

    def __init__(self, v: int, n: Chaine | ChaineVide) -> None:
        self.val = v
        self.next = n

    def tete(self):
        return self.val
    
    def queue(self):
        return self.next

    def est_vide(self):
        return False

    def __repr__(self) -> str:
        return f"{self.val}::{repr(self.next)}"

    def cons(self, v):
        """
        renvoi la chaine "ch" tel que :
        ch.tete() -> v
        ch.queue() -> self
        """
        return Chaine(v, self)

    def append(self, m: Chaine) -> Chaine:
        return Chaine(self, m)
    
    def append_iter(self, m: Chaine) -> None:
        x = self
        while not x.next.est_vide():
            x = x.next
        x.next = m

    def contient(self, x):
        return self.tete() == x or self.queue().contient(x)

    def longueur(self):
        return 1 + self.queue().longueur()

    def maxi(self):
        return max(self.tete(), self.queue().maxi())

    def reverse(self) -> Chaine:
        """
        renvoie la chaîne constituée des mêmes éléments que self
        mais dans l'ordre inverse
        """
        return self.queue().reverse().append(Chaine(self.tete(), ChaineVide()))


    def zip(self, other:Chaine|ChaineVide, res:Chaine|ChaineVide=ChaineVide()) -> Chaine:
        """
        ## Input
        - other: Chaine à zipper avec self
        ## Output 
        - Chaine de tuple contenant forcement 2 variables venant chacun de self et res
        """
        if other.est_vide():
            return res
        return self.queue().zip(other.queue(), res.append(Chaine((self.tete(), other.tete()), ChaineVide())))

    def take(self, n) -> Chaine:
        """
        11::3::7::5::12::().take(1) => 11::()
        11::3::7::5::12::().take(2) => 11::3::()
        11::3::7::5::12::().take(3) => 11::3::7::()
        11::3::7::5::12::().take(7) => 11::3::7::5::12::()
        """
        if n == 0:
            return ChaineVide
        else:
            return Chaine(self.tete(), self.queue().take(n-1))

    def drop(self, n: int) -> Chaine:
        """
        11::3::7::5::12::().drop(1) => 3::7::5::12::()
        11::3::7::5::12::().drop(2) => 7::5::12::()
        11::3::7::5::12::().drop(3) => 5::12::()
        """
        pass


    @staticmethod
    def repeat(n: int, v: int):
        """
        Chaine.repeat(3, 7) => 7::7::7::()
        """
        pass


l = Chaine(5, Chaine(3, Chaine(7, Chaine(1, ChaineVide()))))
ex = Chaine(1, Chaine(2, Chaine(3, ChaineVide())))
print(l.zip(ex))