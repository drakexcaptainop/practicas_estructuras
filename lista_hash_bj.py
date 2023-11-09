from tarea_hmap import hash_tab, clear, wait_key, l8
#Barahona Jorge - Estructuras de Datos 
class hlnode:
    def __init__(self, plato) -> None:
        self.plato = plato 
        self.ingredientes = hash_tab( 31 )
    def __str__(self) -> str:
        fstr =  f'<{self.plato}>['
        for _l8 in self.ingredientes.arr:
            for ing in _l8:
                fstr += ing + ',' 
        
        return fstr.rstrip(',')+']'
        
    def __repr__(self) -> str:
        return f'<{self.plato}>\n'+str(self.ingredientes)+f'\n</{self.plato}>'
        
    pass

class hash_list:
    def __init__(self, N) -> None:
        self.array: list[hlnode] = [None]*N
        self.last = None
        self.N = N

    def insert(self, plato, ingrediente):
        if self.last == self.N:
            return False

        if self.last == None:
            self.last = -1

        nodo_plato= None
        curidx = 0
        while nodo_plato == None and curidx <= self.last:
            if self.array[curidx].plato == plato:
                nodo_plato= self.array[curidx]
            curidx += 1
        
        if nodo_plato is None:
            self.last += 1
            self.array[self.last] = hlnode( plato )
            self.array[self.last].ingredientes.insert( ingrediente )
        
        else:
            nodo_plato.ingredientes.insert( ingrediente )

        return True
    
    def insert_multi(self, plato, ings):
        for ing in ings:
            self.insert( plato, ing )
    
    def search_free_of(self, ingredientes: list):
        curidx = 0
        platos_libres = l8()
        while curidx <= self.last:
            cur_plato = self.array[curidx]
            can_be_served = True
            for ing in ingredientes:
                search_res = cur_plato.ingredientes.search( ing )
                if search_res is not None:
                    can_be_served = False
                    break
            if can_be_served:
                platos_libres.insert_last( cur_plato.plato )
            curidx += 1
        return platos_libres

    def show(self):
        if self.last is None:
            print('[]')
        else:
            curidx = 0
            while curidx <= self.last:
                print( str(self.array[curidx]) )
                curidx += 1

    def search(self, x):
        pass 



hl = hash_list( 10 )
hl.insert_multi( 'hamburguesa', ["carne", "pan", "queso"] )
hl.insert_multi( 'albondiga', ["carne", "arroz", "papa"] )
hl.insert_multi( 'ensalada', ["tomate", "lechuga", "cebolla"] )


menu_str='''
1. Mostrar
2. Insertar Plato/Ingrediente
3. Platos sin ingredientes
'''
def console_loop():
    while (inp:=input(f'{menu_str}\n>>')):
        if inp=='1':
            hl.show()
            wait_key() 
        if inp=='2':
            plato = input('plato>>')
            ings = input("ingredientes (>1 separados por ',')>>").split(',')
            hl.insert_multi(  plato, ings )
        if inp=='3':
            ings = input("ingredientes (>1 separados por ',')>>").split(',')
            hl.search_free_of(ings).show()
            wait_key()
        if inp=='4':
            clear()

console_loop()