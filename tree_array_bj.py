from random import randint as rand

#Barahona Jorge - Estructuras de Datos

class vert:
    def __init__(self, el=None, free=True) -> None:
        self.free = free
        self.el = el
    
    def __repr__(self) -> str:
        return str(self.el)

class tree():
    def __init__(self, N) -> None:
        self.N = N
        self.arr: list[vert] = [vert() for _ in range(self.N)]
    
    def _right(self, idx):
        return idx * 2 + 1
    
    def _left(self, idx):
        return idx * 2
    


    def insert( self, el, pos = 1 ):
        if pos < self.N:
            if self.arr[pos].free:
                self.arr[pos].el = el 
                self.arr[pos].free = False
            else:
                if rand(0, 1):
                    self.insert( el, self._right( pos ) )
                else:
                    self.insert( el, self._left( pos ) )
        

    def insert_in_order(self, el):
        if '__iter__' not in vars(type(el)):
            el = [el]
        iidx = -1
        for i, v in enumerate(self.arr):
            if i<=0: continue
            if v.free:
                iidx = i 
                break
        for i in range( len(el) ):
            self.arr[ iidx + i ].el = el[i] 
            self.arr[ iidx + i ].free = False 
    
    def height(self, idx: int = 1):
        if idx >= self.N or self.arr[ idx ].free:
            return 0
        leftidx, rightidx = self._left( idx ), self._right( idx )
        c1 = self.height( rightidx ) 
        c2 = self.height( leftidx )
        if c1 > c2:
            resp = c1
        else:
            resp = c2 
        return resp + 1

    def count_nodes(self, idx=1):
        if idx >= self.N or self.arr[idx].free:
            return 0
        return self.count_nodes( self._right( idx ) ) + self.count_nodes( self._left( idx ) ) + 1

    

    def show_in_order(self, pos=1):
        if pos < self.N and not self.arr[pos].free:
            self.show_in_order( self._left( pos ) )
            print( f'{self.arr[ pos ].el }',end=' ' )
            self.show_in_order( self._right( pos ) )
    
    def show_post_order(self, pos=1):
        if pos < self.N and not self.arr[pos].free:
            self.show_post_order( self._left( pos ) )
            self.show_post_order( self._right( pos ) )
            print( f'{self.arr[ pos ].el }',end=' ' )


    def show_pre_order(self, pos=1):
        if pos < self.N and not self.arr[pos].free:
            print( f'{self.arr[ pos ].el }',end=' ' )
            self.show_pre_order( self._left( pos ) )
            self.show_pre_order( self._right( pos ) )

    def get_right_most( self, x ):
        
        pass

    def __str__(self) -> str:
        return str(self.arr)
    
    def set_from_array( self, arr ):
        for i, v in enumerate( arr ):
            if v is not None:
                self.arr[i+1].free = False
            self.arr[i+1].el = v

def right( idx ):
    return idx * 2 + 1

def left( idx ):
    return idx * 2

def reflect( target_tree: tree, new_tree: tree = None, olidx: int = 1, nlidx: int = 1 ):
    oli, ori = left(olidx), right(olidx)
    nli, nri = left(nlidx), right(nlidx)
    if olidx >= target_tree.N or oli >= target_tree.N or ori >= target_tree.N:
        return
    if olidx == 1:
        new_tree.arr[ olidx ] = target_tree.arr[ nlidx ]
    new_tree.arr[ nri ], new_tree.arr[ nli ]  = target_tree.arr[ oli ], target_tree.arr[ ori ]
    reflect( target_tree, new_tree, oli, nri )
    reflect( target_tree, new_tree, ori, oli )


t1 = tree( 2**3 )
t2 = tree( t1.N )

t1.set_from_array([2,4,1,7,None,3])
# t1.show_in_order()
# t1.set_from_array([6,3,7,2,5,8,2])


reflect(t1, t2)
t2.show_in_order()
print()
t1.show_in_order()
menu_str = '''
1. Insert Random
2. Height 
3. Count Nodes
4. Show In Order
5. Show Post Order
6. Show Pre Order
'''


def console_loop():
    global t1
    t = t1 
    while (inp:=input(f'{menu_str}\n>>')):
        if inp=='1':
            t.insert( float( input('insert>> ') ) )
        if inp=='2':
            print(t.height())
        if inp=='3':
            print(t.count_nodes())
        if inp=='4':
            t.show_in_order()
        if inp == '5':
            t.show_post_order()
        if inp=='6':
            t.show_pre_order()
    

# console_loop()