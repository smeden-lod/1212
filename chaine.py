"""
implémentations des listes chaînées
"""
from __future__ import annotations

class ChaineVide:
    
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
        pass
    
    
    def reverse(self) -> Chaine:
        """
        """
        pass

    def zip(self, other: Chaine) -> Chaine:
        """
        """
        pass

    def take(self, n) -> Chaine:
        """
        """
        pass

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
        pass
    
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
        pass

    def zip(self, other: Chaine) -> Chaine:
        """
        1::2::3::().zip(8::9::()) => (1, 8)::(2, 9)::()
        1::().zip(8::9::()) => (1, 8)::()
        """
        pass

    def take(self, n) -> Chaine:
        """
        11::3::7::5::12::().take(1) => 11::()
        11::3::7::5::12::().take(2) => 11::3::()
        11::3::7::5::12::().take(3) => 11::3::7::()
        11::3::7::5::12::().take(7) => 11::3::7::5::12::()
        """
        pass

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


l = Chaine(5, Chaine(3, Chaine(7, Chaine(1, ChaineVide()))))
ex = Chaine(1, Chaine(2, Chaine(3, ChaineVide())))