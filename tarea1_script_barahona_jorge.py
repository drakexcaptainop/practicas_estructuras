from os import system
clear = lambda : system('cls')
import numpy as np

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
        return f'<{dtype.__name__}>' + str(self.array) 


arr = array_impl( 5 )



#MENU
dtypemap = {
    'int': int,
    'float': float,
    'str': str
}

dtype = int
class QType:
    ARG_REQUIRED = 1
    NO_ARG_REQUIRED = 0

    def __init__(self, name, type) -> None:
        self.name = name 
        self.T = type
    
    def __get__(self, *_):
        return self.name

class Query:
    INSERT_LAST = QType('insert last', QType.ARG_REQUIRED)
    INSERT_FIRST = QType('insert first', QType.ARG_REQUIRED)
    DELETE_FIRST = QType('delete first', QType.NO_ARG_REQUIRED)
    DELETE_LAST = QType('delete last', QType.NO_ARG_REQUIRED)
    SORT = QType('sort', QType.NO_ARG_REQUIRED)
    SEARCH = QType('search', QType.ARG_REQUIRED)
    NEW = QType('new', QType.ARG_REQUIRED)
    SHOW = QType('show', QType.NO_ARG_REQUIRED)
    RSHOW = QType('rshow', QType.NO_ARG_REQUIRED)
    CAST = QType('cast', QType.ARG_REQUIRED)
    EVAL = QType('eval', QType.ARG_REQUIRED)
    HELP = QType('help', QType.NO_ARG_REQUIRED)
    CLS = QType('cls', QType.NO_ARG_REQUIRED)

    @staticmethod 
    def get_queries( qtype: QType = None ):
        eqfunc = lambda _: True if qtype == None else lambda q: q.T == qtype 
        return ( qt for qt in Query.__dict__.values() if isinstance(qt, QType) and eqfunc( qt ) )

def get_string_args( query: Query, _input: str, parse_dtype = True ):
    if parse_dtype:
        target_func = lambda x: dtype( x.strip() )
    else:
        target_func = str.strip 
    return map(target_func, _input.split(query)[1:])


def bsort(N = 5):
    arr = np.random.randint(0, 10, N)
    print(arr)
    for _ in range(N):
        for i in range(0, N-1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print(arr)

def help_msg():
    print( '\n'.join( (q.name + (" <ARG>" if q.T == QType.ARG_REQUIRED else '')) for q in Query.get_queries(  ) ))




def console_loop():
    global arr, dtype

    help_msg()

    while (inp:=input('>> ')):
        if Query.CLS in inp:
            clear()
            
        if Query.HELP in inp:
            help_msg()

        if Query.EVAL in inp:
            eval(*get_string_args( Query.EVAL, inp, False ), globals())
            continue
        
        if Query.SORT in inp:
            arr.sort()

        if Query.NEW in inp:
            N,= get_string_args( Query.NEW, inp, False )
            arr = array_impl( int( N ) )
            continue

        if Query.DELETE_FIRST in inp:
            arr.delete_first()
        
        if Query.DELETE_LAST in inp:
            arr.delete_last()
        

        try:
            if Query.SEARCH in inp:
                arg ,= get_string_args( Query.SEARCH, inp )
                print( arr.search( arg ) )
            
            if Query.INSERT_LAST in inp:
                arg ,= get_string_args( Query.INSERT_LAST, inp )
                arr.insert_last( arg )

            if Query.INSERT_FIRST in inp:
                arg ,= get_string_args( Query.INSERT_FIRST, inp )
                arr.insert_first( arg )
        except ValueError:
            print(f'Argument cannot be casted to type <{dtype.__name__}>')

        if Query.RSHOW in inp:
            print(arr)
            continue
        
        if Query.SHOW in inp:
            arr.show()
        

        if Query.CAST in inp:
            arg ,= get_string_args( Query.CAST, inp, False )
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
            else:
                print( F'Supported types <{ ", ".join( dtypemap.keys() ) }>' )

console_loop()