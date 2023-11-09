import numpy as np
from os import system

clear = lambda : system('cls')
wait_key = lambda : input('...')


class array_impl:
    def __init__(self, N: int) -> None:
        self.N = N
        self.first = self.last = None
        self.array = [None] * N
    
    def insert_last( self, x ):
        if self.first == None:
            self.first = self.last = self.N // 2 
            self.array[self.last] = x 
        else:
            tmp = self.last
            self.last += 1
            if self.last == self.N:
                self.last = 0
            
            if self.last == self.first:
                self.last = tmp 
            else:
                self.array[self.last] = x 

    def insert_first( self, x ):
        if self.first == None:
            self.insert_last( x )

        else:
            tmp = self.first
            self.first -= 1
            if self.first < 0:
                self.first = self.N - 1
            
            if self.first == self.last:
                self.first = tmp 
            else:
                self.array[ self.first ] = x

    def delete_last( self ):
        if self.first != None:
            if self.last == self.first:
                self.array[ self.last ] = self.first = self.last = None
            else:
                self.array[self.last] = None
                self.last -= 1
                if self.last < 0:
                    self.last = self.N - 1

    def delete_first( self ):
        if self.first != None:
            if self.first == self.last:
                self.array[ self.last ] = self.first = self.last = None
                
            else:
                self.array[ self.first ] = None
                self.first += 1
                if self.first == self.N:
                    self.first = 0

    def cast(self, T: type):
        for i in range(self.N):
            if self.array[i] is None: continue
            self.array[i] = T( self.array[i] )

    def sort( self ):
        if self.first == None or self.first == self.last:
            return
        outer_count = self.first
        while outer_count != self.last:
            i = self.first
            while i != self.last:
                next = i + 1 if i + 1 < self.N else 0
                if self.array[i] > self.array[next]:
                    self.array[i], self.array[next] = self.array[next], self.array[i]
                i = i + 1 if i + 1 < self.N else 0

            outer_count = outer_count + 1 if outer_count + 1 < self.N else 0

    def show( self ):
        if self.first == None:  
            print( '[]' )
        else:
            if self.first == self.last:
                print( self.array[self.first] )
            else:
                i = self.first
                while i != self.last:
                    print( self.array[i], end=', ' )
                    i += 1
                    if i == self.N:
                        i = 0
                print( self.array[i] )
                
        
    
    def search( self, x ):
        if self.first == None:
            return -1
        
        if self.first == self.last and self.array[self.first] == x:
            return 0
        
        offset_index = 0
        i = self.first
        while i != self.last:
            if self.array[i] == x:
                return offset_index 
            i += 1
            offset_index += 1
            if i == self.N:
                i = 0

        return -1 if self.array[self.last] != x else offset_index 
        

    def __str__(self) -> str:
        return f'<first: {self.first}, last: {self.last}, T: {dtype.__name__}>' + str(self.array) 

    def get(self, index):
        return self.array[index]

    @staticmethod 
    def from_list( _list ):
        arr = array_impl( len(_list) )
        for i in _list:
            arr.insert_last( i )
        return arr    

    @staticmethod
    def merge(arr1: 'array_impl', arr2: 'array_impl'):
        new_array = array_impl( arr1.N + arr2.N )
        arr1_index = arr1.first
        arr2_index = arr2.first
        arr1_counter = 0
        arr2_counter = 0
        max_iter = min( arr1.N, arr2.N )

        while arr1_counter < max_iter and arr2_counter < max_iter:
            new_array.insert_last( arr1.get( arr1_index ) )
            arr1_index = arr1_index + 1 if arr1_index + 1 < arr1.N else 0            
            arr1_counter += 1
            new_array.insert_last( arr2.get( arr2_index ) )
            arr2_index = arr2_index + 1 if arr2_index + 1 < arr2.N else 0
            arr2_counter += 1

        while arr1.N != max_iter:
            new_array.insert_last( arr1.get( arr1_index ) )
            arr1_index = arr1_index + 1 if arr1_index + 1 < arr1.N else 0
            if arr1_index == arr1.last:
                new_array.insert_last( arr1.get( arr1_index ) )
                break

                
        while arr2.N != max_iter:
            new_array.insert_last( arr2.get( arr2_index ) )
            arr2_index = arr2_index + 1 if arr2_index + 1 < arr2.N else 0
            if arr2_index == arr2.last:
                new_array.insert_last( arr2.get( arr2_index ) )
                break

        return new_array
             

dtype = int

l1, l2 = array_impl.from_list( 'abcd' ), array_impl.from_list( 'xy' )

print(l1)
print(l2)
arr = array_impl.merge( l1, l2 )


#MENU
dtypemap = {
    'int': int,
    'float': float,
    'str': str
}

print(arr)
menu_str = '''1. Insert First
2. Insert Last
3. Delete First
4. Delete Last
5. Show
6. Search
7. Sort (Burbuja)
8. Array View
9. Cast
10. New Array'''


def console_loop():
    global arr, dtype
    while (inp:=input(f'{menu_str}\n>> ')):
        clear()
        if inp == '1':
            arg = dtype(input(f'{dtype.__name__}>> '))
            arr.insert_first( arg )
        elif inp == '2':
            arg = dtype(input(f'{dtype.__name__}>> '))
            arr.insert_last( arg )
        elif inp=='3':
            arr.delete_first()
        elif inp=='4':
            arr.delete_last()
        elif inp=='5':
            arr.show()
            wait_key()
        elif inp=='6':
            arg = dtype(input(f'{dtype.__name__}>> '))
            print( arr.search( arg ) )
            wait_key()
        elif inp=='7':
            arr.sort()

        elif inp=='8':
            print(arr)
            wait_key()
        elif inp=='9':
            arg = input( F'Supported types <{ ", ".join( dtypemap.keys() ) }>\n>> ' )
            T = dtypemap.get( arg, False )
            
            if T:
                if T == dtype:
                    continue 
                try:
                    arr.cast( T )
                    dtype = T
                except ValueError:
                    print( f'Array cannot be casted to type <{T.__name__}>' )
                    arr.cast( dtype )
                    wait_key()
                

        elif inp=='10':
            N = int(input( 'New Array Size\n>> ' ))
            arr = array_impl( int( N ) )
        clear()

console_loop()