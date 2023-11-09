import os
#barahona jorge - estructuras de datos
clear = lambda : os.system('cls')
wait_key = lambda : input('...')

class node:
    def __init__(self, el, height=0, right=None,left=None) -> None:
        self.el = el
        self.right: 'node' = right
        self.left: 'node' = left
        self._height=height
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}<el={self.el}, left={not not self.left}, right={not not self.right}>'
    
    @staticmethod
    def height( _node: 'node' ):
        height_left= (_node.left._height) if _node.left else 0
        height_right= (_node.right._height ) if _node.right else 0
        return max( height_left, height_right ) + 1
    @staticmethod
    def balance_factor( _node: 'node' ):
        height_left= (_node.left._height) if _node.left else 0  
        height_right= (_node.right._height) if _node.right else 0
        return height_left - height_right 

         

class redblack_node:
    pass
class avl:
    def __init__(self) -> None:
        self.head = None
    
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
        pass
    
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


    
    def insert_avl(self, el, avl_node: node, ):
        if self.head == None:
            self.head = node( el, 1 )
        else:
            if el < avl_node.el:
                if avl_node.left is None:
                    avl_node.left = node( el, 1 )
                else:
                    has_rotated, new_child = self.insert_avl( el, avl_node.left )
                    if has_rotated:
                        avl_node.left = new_child

            elif el > avl_node.el:
                if avl_node.right is None:
                    avl_node.right = node( el, 1 )
                else:
                    has_rotated, new_child = self.insert_avl( el, avl_node.right )
                    if has_rotated:
                        avl_node.right = new_child

            avl_node._height = node.height( avl_node )
            bfactor = node.balance_factor( avl_node )

            return_node = None
            has_rotated = False
            if bfactor == 2:
                if node.balance_factor( avl_node.left ) == 1:
                    return_node = self.ll_rot( avl_node )
                    has_rotated = True
                elif node.balance_factor( avl_node.left ) == -1:
                    return_node = self.lr_rot( avl_node )
                    has_rotated = True

            elif bfactor == -2:
                if node.balance_factor( avl_node.right ) == -1:
                    return_node = self.rr_rot( avl_node )
                    has_rotated = True
                elif node.balance_factor( avl_node.right ) == 1:
                    return_node = self.rl_rot( avl_node )
                    has_rotated = True

            return has_rotated, return_node

    
    def ll_rot( self, imbalaced_node: 'node' ):
        new_head = imbalaced_node.left
        new_head_right_tmp = new_head.right

        new_head.right = imbalaced_node
        imbalaced_node.left = new_head_right_tmp

        new_head.right._height = node.height( new_head.right )
        new_head._height = node.height( new_head )

        if self.head == imbalaced_node:
            self.head = new_head

        return new_head

    def lr_rot( self, imbalanced_node: 'node' ):
        new_head = imbalanced_node.left.right
        new_head_tmp_left = new_head.left
        new_head_tmp_right = new_head.right

        new_head.left = imbalanced_node.left
        new_head.right = imbalanced_node
        
        imbalanced_node.left = new_head_tmp_right
        new_head.left.right = new_head_tmp_left

        if imbalanced_node == self.head:
            self.head = new_head
        
        new_head.left._height = node.height( new_head.left )
        new_head.right._height = node.height( new_head.right )
        new_head._height = node.height( new_head )

        return new_head

    def rr_rot( self, imbalaced_node: 'node' ):
        new_head = imbalaced_node.right
        new_head_left_tmp = new_head.left

        new_head.left = imbalaced_node
        new_head.left.right = new_head_left_tmp

        new_head.left._height = node.height( new_head.left )
        new_head._height = node.height( new_head )

        if imbalaced_node == self.head:
            self.head = new_head
        
        return new_head
    
    def rl_rot( self, imbalanced_node: 'node' ):
        new_head = imbalanced_node.right.left
        new_head_tmp_right = new_head.right
        new_head_tmp_left = new_head.left
        
        new_head.left = imbalanced_node
        new_head.right = imbalanced_node.right

        new_head.left.right = new_head_tmp_left
        new_head.right.left = new_head_tmp_right

        new_head.right._height = node.height( new_head.right )
        new_head.left._height = node.height( new_head.left )
        new_head._height = node.height( new_head )

        if self.head == imbalanced_node:
            self.head = new_head
        
        return new_head


    def __len__(self):
        return self.count_nodes(  )
    

def loadtree(  ):
    path = 'C:\\Users\\juggb\\Downloads\\src\\DL\\tareas_structurasdd\\nums.txt'
    tree = avl()
    with open(path,'r') as f:
        for line in (f):
            tree.insert_avl( int(line), tree.head)
    return tree



def count_factor_nodes( _node: node, cache: list ):
    if _node is None:
        return
    factor = node.balance_factor( _node )
    cache[factor+1]+=1
    count_factor_nodes( _node.left, cache )
    count_factor_nodes( _node.right, cache )
    

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
tree = avl(  )
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
            tree.insert_avl( T(input()), tree.head )
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
            print('not implemented')
        if inp=='10':
            arg = T( input() )
            print( tree.search( arg ) )
        if inp=='11':
            print('not implemented')

        if inp=='12':
            tree=loadtree(  )
            print('loaded!')
        wait_key()
        clear()


tree = loadtree()

cache=[0]*3
count_factor_nodes( tree.head, cache )
print(cache)
print(sum(cache))