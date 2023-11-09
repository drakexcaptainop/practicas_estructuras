import os
#barahona jorge - estructuras de datos
clear = lambda : os.system('cls')
wait_key = lambda : input('...')

class node:
    def __init__(self, el, free = True) -> None:
        self.el = el 
        self.free = free  
    
    def __repr__(self) -> str:
        return str(self.el)

class heap_min:
    def __init__(self, N) -> None:
        self.arr: list[node] = [(node(0) if i != 0 else None) for i in range(N+1)]
        self.N = N
        self.last_leaf = 0

    def insert( self, el ):
        if self.last_leaf == 0:
            self.last_leaf = 1
            self.arr[self.last_leaf].el = el
            self.arr[self.last_leaf].free = False 
        else:
            self.last_leaf += 1
            self.arr[self.last_leaf].el = el 
            self.arr[self.last_leaf].free = False
            self.bottom_up_balance(self.last_leaf)
    
    def bottom_up_balance(self, i):
        if i > 1:
            parent_index = i//2
            if self.arr[ parent_index ].el > self.arr[ i ].el:
                self.arr[ parent_index ].el, self.arr[ i ].el = self.arr[i].el, self.arr[parent_index].el
                self.bottom_up_balance( parent_index )

    def print_in_order( self, i=1 ):
        if i>self.N:
            return
        self.print_in_order( i*2 )
        if not self.arr[i].free:
            print(self.arr[i].el,end=', ')
        self.print_in_order( i*2 + 1 )
    
    def delete_top(self):
        el = self.arr[1].el

        if self.last_leaf == 1:
            self.arr[self.last_leaf].free = True
            self.last_leaf = 0
        else:
            self.arr[1].el=self.arr[self.last_leaf].el 
            self.arr[self.last_leaf].free = True
            self.last_leaf -= 1
            self.top_down_balance(1)
        return el 

    def top_down_balance(self, i: int):
        left_idx = i*2

        # if (i.bit_length() - 1) < (self.last_leaf.bit_length() - 1):
        if left_idx <= self.last_leaf:
            right_idx = i*2+1
            
            swap_index = -1
            if right_idx > self.last_leaf:
                swap_index = left_idx
            else:
                if self.arr[left_idx].el < self.arr[right_idx].el:
                    swap_index = left_idx 
                else:
                    swap_index = right_idx
            if self.arr[i].el > self.arr[swap_index].el:
                self.arr[i].el, self.arr[swap_index].el = self.arr[swap_index].el, self.arr[i].el 
                self.top_down_balance(swap_index)

    def height(self):
        return self.last_leaf.bit_length() - 1
    
    def count_nodes(self):
        return self.last_leaf
    
    def sort(self):
        sorted_arr = []
        while self.last_leaf != 0:
            el = self.delete_top()
            sorted_arr.append( el )
        return sorted_arr
    
        

menu_str = ['insert',
'node count',
'height',
'delete top',
'show In Order',
'show array',
'heap sort',
]
tree = heap_min( 10 )
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
            for v in map(T, input().split(',')):
                tree.insert( v )
        if inp=='2':
            print(tree.count_nodes())
        if inp=='3':
            print(tree.height())
        if inp =='4':
            print(tree.delete_top())
        if inp =='5':
            tree.print_in_order()
            print()
        if inp == '6':
            print(tree.arr)
        if inp == '7':
            print(tree.sort())
        
        wait_key()
        clear()




# console_loop()