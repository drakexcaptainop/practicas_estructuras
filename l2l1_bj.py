import os
#barahona jorge - estructuras de datos
clear = lambda : os.system('cls')
wait_key = lambda : input('...')
PATH  ='C:\\Users\\juggb\\Downloads\\src\DL\\tareas_structurasdd\\paises.txt'


class l1:
    def __init__(self, size) -> None:
        self.last = -1
        self.N = size
        self.array = [ None ] * size

    def __getitem__(self, i):
        return self.array[i]

    def insert_last(self, x):
        if self.last < self.N:
            self.last += 1
            self.array[self.last] = x          

    def delete_last(self):
        if self.last >= 0:
            self.last -= 1
    
    def show(self):
        return print(self.repr())
    
    def repr(self):
        rstr = '['
        cur = 0
        while cur <= self.last:
            rstr += '{0}{1}'.format( self.array[cur], ', ' if cur < self.last else '' )
            cur += 1
        return rstr+']'
    


    def search(self, x):
        cur = 0
        while cur <= self.last:
            if self.array[cur] == x:
                return cur 
            cur += 1
        return -1

class crit:
    __slots__ = [ 'l1lista', 'crit' ]
    def __init__(self, crit, N) -> None:
        self.crit = crit
        self.l1lista = l1( N )

    def __str__(self) -> str:       
        return f'{self.crit}'
class l2l1:
    def __init__(self, N: int, l1_size = 10) -> None:
        self.N = N
        self.first = self.last = None
        self.array: list[crit] = [None] * N
        self.l1_size = l1_size
    
    def l2l1_insert_last(self, crite, name):
        if not (self.first == 0 and self.last == self.N - 1):
            if self.first == None:
                self.first = self.last = self.N // 2
                ncrit = crit( crite, self.l1_size )
                
                self.array[self.first] = ncrit
                self.array[self.first].l1lista.insert_last( name )
            
            else:
                aux = self.first
                while crite != self.array[ aux ].crit and aux != self.last:
                    aux = (aux + 1) % self.N
                
                if crite == self.array[aux].crit:
                    self.array[aux].l1lista.insert_last( name )
                else:
                    if self.last == self.N - 1:
                        self.last = 0
                    else:
                        self.last += 1
                    if self.first != self.last:
                        ncrit = crit( crite, self.l1_size )
                        self.array[self.last] = ncrit
                        self.array[self.last].l1lista.insert_last( name )
                    else:
                        self.last -= 1

    def l2l1_insert_first(self, crite, name):
       if not (self.first == 0 and self.last == self.N - 1):
            if self.first == None:
                self.first = self.last = self.N // 2
                ncrit = crit( crite, self.l1_size )
                
                self.array[self.first] = ncrit
                self.array[self.first].l1lista.insert_last( name )
            
            else:
                aux = self.first
                while crite != self.array[ aux ].crit and aux != self.last:
                    aux = (aux + 1) % self.N
                
                if crite == self.array[aux].crit:
                    self.array[aux].l1lista.insert_last( name )
                else:
                    if self.first == 0:
                        self.first = self.N - 1
                    else:
                        self.first -= 1
                    if self.first != self.last:
                        ncrit = crit( crite,self.l1_size )
                        self.array[self.first] = ncrit
                        self.array[self.first].l1lista.insert_last( name )
                    else:
                        self.first += 1

    def l2l1_delete_last(self):
        if self.first != None:
            if self.first == self.last:
                self.first = self.last = None
            
            else:
                if self.last == 0:
                    self.last = self.N - 1
                else:   
                    self.last -= 1
    
    def l2l1_delete_first(self):
        if self.first != None:
            if self.first == self.last:
                self.first = self.last = None
            
            else:
                if self.first == self.N - 1:
                    self.first = 0
                else:   
                    self.first += 1
    

    def search( self, _crit ):
        if self.first == None:
            return -1
        
        cur = self.first
        while cur != self.last:
            if self.array[cur].crit == _crit:
                return cur 
            cur = (cur + 1)%self.N 
        
        return cur if self.array[cur].crit == _crit else -1
    
    def search_el(self, _crit, val):
        idx = self.search( _crit )
        if idx != -1:
            inner_index = self.array[idx].l1lista.search( val )
            if inner_index != -1:
                return [self.array[idx].crit, idx, inner_index]
            

    def show_crit(self, _crit):
        if self.first == None:
            print('[]')
        else:
            cur = self.first
            while cur != self.last:
                if self.array[cur].crit == _crit:
                    print(f'<{_crit}>',end='')
                    print(self.array[cur].l1lista.repr())
                cur = (cur+1)%self.N
                
            
            if self.array[self.last].crit== _crit:
                print(f'<{_crit}>',end='')
                print(self.array[cur].l1lista.repr())

    def __str__(self) -> str:
        return f'<first: {self.first}, last: {self.last}, size: {self.N}>[' + ','.join( str(_crit) for _crit in self.array if _crit != None)+']'

    def __repr__(self) -> str:
        return str(self)
    def show(self):
        if self.first == None:
            return print('[]')
        
        cur = self.first
        while cur != self.last:
            print( f'<{self.array[cur].crit}>{self.array[cur].l1lista.repr()}')
            cur = (cur+1) % self.N
        
        print( f'<{self.array[cur].crit}>{self.array[cur].l1lista.repr()}')
        


    def get(self, index):
        return self.array[index]

dtype = lambda _:_

#MENU
dtypemap = {
    'int': int,
    'float': float,
    'str': str
}

arr = l2l1( 5 )



menu_str = '''1. Insert First
2. Insert Last
3. Delete First
4. Delete Last
5. Show
6. Show Crit
7. Search
8. Search El
'''



def load_data():
    lista = l2l1( 100 )
    with open( PATH, 'r', encoding='utf-8' ) as f:
        for i in f:
            split_list =  i.strip('\n').split(' ')
            for i in range(1, len(split_list)):
                lista.l2l1_insert_first( split_list[0], split_list[i] )
    return lista

def search_max( lista: l2l1 ):
    l_countries = l2l1( 100, 100 )
    cur = lista.first
    while cur != lista.last+1:
        _crit: crit = lista.get( cur )
        cur_inner = 0
        while cur_inner <= _crit.l1lista.last:
            country =_crit.l1lista[cur_inner]
            l_countries.l2l1_insert_last( country, _crit.crit )
            cur_inner += 1
        cur = (cur + 1) % lista.N
    
    cur = l_countries.first
    max = None
    cur_crit = ''
    l_countries.show()
    while cur != l_countries.last + 1:
        if max == None:
            cur_crit = l_countries.get( cur ).crit
            max = l_countries.get( cur ).l1lista.last
        else:
            tmp = l_countries.get( cur ).l1lista.last
            if tmp > max:
                cur_crit = l_countries.get( cur ).crit
                max = tmp 
        cur = (cur + 1)%l_countries.N
    
    return l_countries, max+1, cur_crit



def console_loop():
    global arr
    while (inp:=input(f'{menu_str}\n>> ')):
        clear()
        if inp == '1':
            crit = input('crit>> ')
            name = input('name>> ') 
            arr.l2l1_insert_first( crit, name )
        elif inp == '2':
            crit = input('crit>> ')
            name = input('name>> ') 
            arr.l2l1_insert_last( crit, name )

        elif inp=='3':
            arr.l2l1_delete_first()
        elif inp=='4':
            arr.l2l1_delete_last()
        elif inp=='5':
            arr.show()
            wait_key()
        elif inp=='6':
            arg = input('crit>>'  )
            arr.show_crit( arg  )
            wait_key()
        elif inp=='7':
            arg = input( 'crit>> ' )
            print(arr.search( arg ))
            wait_key()

        elif inp=='8':
            arg1, arg2 = input('el>> '), input('crit>> ')
            print(arr.search_el( arg2, arg1 ))
            wait_key()
        elif inp=='9':
            eval(input('>> '))
            wait_key()
        clear()

#console_loop()
l = load_data()
lista, participaciones, pais = search_max( l )
print(F'{participaciones = }\n{pais = }')