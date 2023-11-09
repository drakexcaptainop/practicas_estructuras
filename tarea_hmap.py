try:
    from tarea_lista_impl8_bj import l8, clear, wait_key
except ImportError:
    print( ' se necesita correr desde el mismo directorio en el que se encuentra el archivo {0} '.format(__file__) )
    quit(1)
    
##Barahona Jorge - Structuras de Datos
PATH  ='C:\\Users\\juggb\\Downloads\\src\DL\\tareas_structurasdd\\paises.txt'




class hash_tab:
    def __init__(self, N) -> None:
        self.N = N
        self.arr = [l8() for _ in range(self.N)]

    def insert( self, el: str ):
        pos = self.pos( el )
        cur_lis = self.arr[pos]
        # if cur_lis.search( el ) is None:
        cur_lis.insert_last( el )

    def delete( self, el: str ):
        pos = self.pos( el )
        cur_lis = self.arr[ pos ]
        # deleted = False
        # if cur_lis.first != None:
        #     if cur_lis.first.el == el:
        #         deleted = cur_lis.delete_first()
        #     else:
        #         if cur_lis.last.el == el:
        #             deleted = cur_lis.delete_last()
        #         else:
        #             cur = cur_lis.first
        #             while cur != cur_lis.last and cur.el != el:
        #                 cur = cur.next
                    
        #             if cur != None and cur.el == el:
        #                 cur.prev.next = cur.next
        #                 deleted = True
        return cur_lis.delete( el )
                        
    def search(self, el):
        pos = self.pos(el)
        cur_lis = self.arr[pos]
        cur_lis_index = cur_lis.search( el )
        return (pos, cur_lis_index) if cur_lis_index is not None else cur_lis_index
            
    def __str__(self):
        return str(self.arr)

    def pos(self, x: str):
        pos = 0
        for i in range(len(x)):
            pos += ord( x[i] ) * 5 ** i
        return pos % self.N 
    
    def delete_all( self, x ):
        cur_lis = self.arr[ self.pos( x ) ]
        outf = cur_lis.delete(x)
        while True:
            tmp = cur_lis.delete(x)
            if not tmp:
                break
        return outf
    
        
menu_str = '''1. Insert
2. Delete
3. Search
4. Array View
5. Del All
'''
                    

# h = hash_tab(10)
# h.insert('asd0')
# h.insert('asd1')
# h.insert('asd2')
# h.insert('asd3')
# h.insert('asd4')
# h.insert('asd5')
# print(str(h))


def count_collision( ht: hash_tab ):
    ccount = [0]*50
    for li in ht.arr:
        ccount[ li.size() ] += 1
    return ccount

def load_data(dictt=False):
    lista = hash_tab( 53 if not dictt else 56783 )

    if dictt:
        with open( 'C:\\Users\\juggb\\Downloads\\src\\DL\\tareas_structurasdd\\dictnp.txt', 'r', encoding='utf-8' ) as f:
            arr = f.read().split('\n')
            print(len(arr))
            for i in arr:
                lista.insert(i )
    else:
        with open( PATH, 'r', encoding='utf-8' ) as f:
            for i in f:
                split_list =  i.strip('\n').split(' ')
                for i in range(1, len(split_list)):
                    lista.insert(split_list[i] )
    return lista


h = load_data(1)
# print(str(h))

print(sum((i+1)*v for i, v in enumerate(count_collision(h)[1:])))
def console_loop():
    while (inp:=int(input(f'{menu_str}\n>>') or 0)):
        if inp == 1:
            arg = input('insert>> ')
            h.insert( arg )
        if inp == 2:
            arg = input('delete>> ')
            print(h.delete( arg ))
        if inp == 3:
            arg = input('search>> ')
            print(h.search( arg ))
        if inp == 4:
            print( str(h) )
        if inp == 5:
            arg = input('delete_all>> ')
            print(h.delete_all( arg ))
        if inp==6:
            clear()
        wait_key()
    return
    while (inp:=input('>> ')):
        if 'insert' in inp:
            el = inp.split(' ')[-1]
            h.insert( el )
        
        if 'delete' in inp:
            el = inp.split(' ')[-1]
            h.delete(el)

        if 'search' in inp:
            el = inp.split(' ')[-1]
            print(h.search(el))
        
        if 'view' in inp:
            print(h)
        
        if 'cls' in inp:
            clear()
        

# console_loop()