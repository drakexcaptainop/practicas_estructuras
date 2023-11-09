import os
#barahona jorge - estructuras de datos
clear = lambda : os.system('cls')
wait_key = lambda : input('...')

class node:
    def __init__(self, el, right=None,left=None) -> None:
        self.el = el 
        self.right: 'node' = right
        self.left:'node' = left
    
    def delete_node( self, ref ):
        if ref == self.right:
            self.right = None
        if ref == self.left:
            self.left = None
        del ref
    
    def __repr__(self) -> str:
        return f'node({self.el}, right={not not self.right}, left={not not self.left})'
class COLOR:
    BLACK = 'black'
    RED = 'red'
class SIDE:
    LEFT = 'L'
    RIGHT = 'R'
class redblack_node(node):
    
    def __init__(self, *args, color: COLOR = COLOR.RED) -> None:
        node.__init__(self, *args)
        self.color = color 
    
    def __repr__(self) -> str:
        return super().__repr__().rstrip(')')+f', color={self.color})'


class abb:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, el):
        return self._insert( el, self.head )
    def get(self, el):
        return self._search(el, self.head)
    
    def _search(self, el, _node: node):
        flag = False
        if _node is not None:
            if _node.el == el:
                flag = True
            else:
                if el < _node.el:
                    flag = self._search(el, _node.left)
                else:
                    flag = self._search(el, _node.right)    
        return flag

    def _insert(self, el, _node: node):
        if self.head is None:
            self.head = node( el )
        else:
            if _node is None:
                return node( el )
            else:
                if el < _node.el:
                    new_node = self._insert( el, _node.left )
                    if new_node is not None:
                        _node.left = new_node
                elif el > _node.el:
                    new_node = self._insert( el, _node.right )
                    if new_node is not None:
                        _node.right = new_node
    def min(self):
        return self._min( self.head )

    def max(self):
        return self._max(self.head)

    def _min(self, _node: node):
        if _node is None:
            return None
        if _node.left is None:
            return _node.el 
        else:
            return self._min( _node.left )


    def _max(self, _node):
        if _node is None:
            return None
        if _node.right is None:
            return _node.el 
        else:
            return self._max( _node.right )

    def delete(self, el):
        return self._delete(el, self.head, None)

    def _delete(self, el, _node: node, _parent: node):
        if _node is None:
            return False
        else:
            if el < _node.el:
                flag = self._delete( el, _node.left, _node )
            elif el > _node.el: 
                flag = self._delete( el, _node.right, _node )
            else:
                if _node.left is None and _node.right is None:
                    if _parent != None:
                        _parent.delete_node( _node )
                    if self.head == _node:
                        self.head = None
                    flag = True
                else:
                    if _node.right is not None:
                        replace_elem = self._min( _node.right )
                        _node.el = replace_elem
                        flag = self._delete( replace_elem, _node.right, _node )
                    else:
                        if _node.left is not None:
                            replace_elem = self._max( _node.left )
                            _node.el = replace_elem
                            flag = self._delete( replace_elem, _node.left, _node )
            return flag
    
    def _count_nodes(self, _node):
        if _node is None:
            return 0 
        return self._count_nodes( _node.right ) + self._count_nodes( _node.left ) + 1
     
    def count_nodes( self ):
        return self._count_nodes( self.head )
    
    def _height(self, _node: node):
        if _node is None:
            return 0 
        lheight = self._height( _node.left )
        rheight = self._height( _node.right )
        if  lheight < rheight:
            return rheight + 1
        return lheight + 1
        
        
    def height( self ):
        return self._height(self.head )

        
    def print_in_order(self, _node=True):
        if self.head is None:
            print('[]')
        else:
            if _node == True:
                _node = self.head
            if _node is None:
                return
            
            self.print_in_order( _node.left )
            print(_node.el,end=',')
            self.print_in_order(  _node.right )

    def print_post_order(self, _node=True):
        if self.head is None:
            print('[]')
        else:
            if _node == True:
                _node = self.head
            if _node is None:
                return
            
            self.print_post_order( _node.left )
            self.print_post_order(  _node.right )
            print(_node.el,end=',')

    def print_pre_order(self, _node=True):
        if self.head is None:
            print('[]')
        else:
            if _node == True:
                _node = self.head
            if _node is None:
                return
            print(_node.el,end=' ')
            self.print_pre_order( _node.left )
            self.print_pre_order(  _node.right )


    def insert_inverse(self, el, _node: node):
        if self.head is None:
            self.head = node( el )
        else:
            if _node is None:
                return node( el )
            else:
                if el > _node.el:
                    new_node = self.insert_inverse( el, _node.left )
                    if new_node is not None:
                        _node.left = new_node
                elif el < _node.el:
                    new_node = self.insert_inverse( el, _node.right )
                    if new_node is not None:
                        _node.right = new_node


    def insert_red_black( self, el, rbnode: redblack_node, parent: redblack_node, call_side: SIDE=None ):
        cont=False
        par=False
        side=None
        if rbnode is None and parent is None:
            self.head = redblack_node( el, color=COLOR.BLACK )
        else:
            if el < rbnode.el:
                if rbnode.left is None:
                    par = cont = True 
                    rbnode.left = redblack_node( el, color=COLOR.RED )
                
                else:
                    par, cont, side = self.insert_red_black( el, rbnode.left, rbnode, call_side=SIDE.LEFT )
                
                if cont: 
                    if par == True:
                        if rbnode.color == COLOR.BLACK:
                            cont = False
                        else:
                            par = False
                            side = SIDE.LEFT
                    else:
                        if rbnode.right != None and rbnode.right.color == COLOR.RED:
                            rbnode.left.color = COLOR.BLACK
                            rbnode.right.color = COLOR.BLACK
                            rbnode.color = COLOR.RED
                            par = True
                        else:
                            cont = False
                            if side == SIDE.RIGHT:
                                self.rot_left( rbnode.left, rbnode, SIDE.LEFT )
                            rbnode.left.color = COLOR.BLACK
                            rbnode.color = COLOR.RED
                            self.rot_right( rbnode, parent, call_side )

            elif el > rbnode.el:
                if rbnode.right is None:
                    par = cont = True 
                    rbnode.right = redblack_node( el, color=COLOR.RED )
                
                else:
                    par, cont, side = self.insert_red_black( el, rbnode.right, rbnode, call_side=SIDE.RIGHT )
                
                if cont: 
                    if par == True:
                        if rbnode.color == COLOR.BLACK:
                            cont = False
                        else:
                            par = False
                            side = SIDE.RIGHT
                    else:
                        if rbnode.left != None and rbnode.left.color == COLOR.RED:
                            rbnode.right.color = COLOR.BLACK
                            rbnode.left.color = COLOR.BLACK
                            rbnode.color = COLOR.RED
                            par = True
                        else:
                            cont = False
                            if side == SIDE.LEFT:
                                self.rot_right( rbnode.right, rbnode, SIDE.RIGHT )
                            rbnode.right.color = COLOR.BLACK
                            rbnode.color = COLOR.RED
                            self.rot_left( rbnode, parent, call_side )
                            
        return par, cont, side 

    
    def rot_right(self, rbnode: redblack_node, parent: redblack_node, side: SIDE):
        if parent != None:
            if side == SIDE.RIGHT:
                parent.right = rbnode.left
            else:
                parent.left = rbnode.left
        else:
            self.head = rbnode.left

        if rbnode.left.right != None:
            tmp = rbnode.left.right
        else:
            tmp = None

        rbnode.left.right = rbnode  
        rbnode.left = tmp

    def rot_left(self, rbnode: redblack_node, parent: redblack_node, side: SIDE):
        if parent != None:
            if side == SIDE.RIGHT:
                parent.right = rbnode.right
            else:
                parent.left = rbnode.right
        else:
            self.head = rbnode.right

        if rbnode.right.left != None:
            tmp = rbnode.right.left
        else:
            tmp = None

        rbnode.right.left = rbnode  
        rbnode.right = tmp
    
    def insertrb(self, el):
        self.insert_red_black( el, self.head, None )

    def __setitem__(self, el, _):
        self.insertrb( el )

    def __len__(self):
        return self.count_nodes(  )

import time 
def loadtree( tree, isrb=False ):
    time_start = time.perf_counter( ) 
    path = 'C:\\Users\\juggb\\Downloads\\src\\DL\\tareas_structurasdd\\nums.txt'
    try:
        with open(path,'r') as f:
            for i, line in enumerate(f):
                if isrb:
                    tree[int(line)] = int(line)
                else:
                    tree.insert( int( line ) )
        time_end = time.perf_counter()
        return tree, time_end - time_start
    except Exception as e:
        print(f'Error in loading {line}, {e}')

menu_str = ['insert',
'node count',
'height',
'min',
'max',
'show In Order',
'show Pre Order',
'show Post Order',
'delete',
'search',
'reflect',
'Load Data',
''
]
tree = abb(  )
T=int
def console_loop():
    global tree
    while (inp:=input('{0}\n>> '.format( "\n".join(F'{i+1}. {v}' for i,v in enumerate(menu_str)) ))):
        try:
            opt=menu_str[int(inp)-1]
            print(f'{opt}>> ',end='')
        except ValueError:
            opt='error'
        if inp=='1':
            tree.insertrb( T(input()) )
        if inp=='2':
            print(tree.count_nodes())
        if inp=='3':
            print(tree.height())
        if inp =='4':
            print(tree.min())
        if inp =='5':
            print(tree.max())
        if inp =='6':
            tree.print_in_order()
            print()
        if inp =='7':
            tree.print_pre_order()
            print()
        if inp =='8':
            tree.print_post_order()
            print()
        if inp=='9':
            tree.delete( T(input('')) )
        if inp=='10':
            arg = T( input() )
            print( tree.search( arg ) )
        if inp=='11':
            print('not implemented')

        if inp=='12':
            tree=loadtree( abb(  ), isrb=True )
            print('loaded!')
        wait_key()
        clear()


def timesearch( tree ):
    import numpy.random as ran 
    min, max = 0, len(tree)
    start = time.perf_counter()
    for _ in range(int(1e6)):
        tree.get( ran.randint( min, max ) )
    return time.perf_counter() - start

     

dtree = dict(  )
arn = abb(  )

tree, load_time_map = loadtree( dtree, True )
arn, load_time_arn = loadtree( arn, True )

print(arn.count_nodes())
print(arn.height())



with open('C:\\Users\\juggb\\Downloads\\src\\DL\\tareas_structurasdd\\nums.txt', 'r') as f:
    x=set()
    for i in f:
       x.add( int(i) )
       x.add(int(i))
    print(f'{len(x)=}')
