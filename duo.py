class duo:
    __slots__ = ['vert', 'dist']
    def __init__(self, vert, dist = None) -> None:
        self.vert = vert 
        self.dist = dist
    
    def __lt__(self, other: 'duo'):
        return self.dist < other.dist
    
class Inf:
    def __le__(self, _):
         return False

    def __ge__(self, _):
        return True
    
    def __lt__(self, _):
        return False
    
    def __gt__(self, _):
        return True
    
    def __eq__(self, _: object) -> bool:
        return False

inf = Inf()
