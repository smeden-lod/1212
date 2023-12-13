class Maillon:

    def __init__(self, v, n) -> None:
        self.val = v
        self.next = n
    
class CList:

    def __init__(self, d: Maillon | None):
        self.debut = d

    def is_empty(self):
        return self.debut is None
    
    def head(self):
        if self.is_empty():
            raise ValueError
        return self.debut.val

    def tail(self):
        if self.is_empty():
            return CList(None)
        return CList(self.debut.next)

    def __repr__(self):
        if self.is_empty():
            return "()"
        return f"({self.head()},{repr(self.tail())})"
    
def list2Maillon(l):
    if l == []:
        return None
    return Maillon(l[0], list2Maillon(l[1:]))

l = Maillon(5, Maillon(3, Maillon(7, Maillon(1, None))))