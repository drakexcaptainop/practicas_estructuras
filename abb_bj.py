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

class abb:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, el):
        return self._insert( el, self.head )

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
        return _node.el if _node.left is None else self._min( _node.left ) 


    def _max(self, _node):
        if _node is None:
            return None
        return _node.el if _node.right is None else self._max( _node.right ) 
        

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

    def search(self, el):
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
    def __len__(self):
        return self.count_nodes(  )
tree = abb()
tree.insert( 1 )
tree.insert( 2)
tree.insert( 3 )
tree.insert( 4 )
tree.insert( 5 )
tree.insert( 6 )

tree.delete(6)



def reflect( current_node: node, new_tree: abb = None ):
    if current_node is None:
        return
    new_tree.insert_inverse( current_node.el )
    reflect( current_node.left, new_tree )
    reflect( current_node.right, new_tree )
    



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

T = int 


def reflect( current_node: node, new_tree: abb = None ):
    if current_node is None:
        return
    new_tree.insert_inverse( current_node.el, new_tree.head )
    reflect( current_node.left, new_tree )
    reflect( current_node.right, new_tree )
    
def load_2_tree():
    path = 'C:\\Users\\juggb\\Downloads\\src\\DL\\tareas_structurasdd\\nums.txt'
    loaded_tree = abb()
    try:
        with open(path,'r') as f:
            for line in f:
                loaded_tree.insert( int( line ) )
        return loaded_tree
    except:
        print(f'Error in loading file "{path}"')

def console_loop():
    global tree
    while (inp:=input('{0}\n>> '.format( "\n".join(F'{i+1}. {v}' for i,v in enumerate(menu_str)) ))):
        try:
            opt=menu_str[int(inp)-1]
            print(f'{opt}>> ',end='')
        except ValueError:
            opt='error'
        if inp=='1':
            tree.insert( T(input()) )
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
            new_tree = abb()
            reflect( tree.head, new_tree )
            new_tree.print_in_order()
            print()

        if inp=='12':
            tree=load_2_tree()
            print('loaded!')
        wait_key()
        clear()

console_loop()