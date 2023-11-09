from tarea_lista_impl8_bj import l8_queue, clear, wait_key
#Barahona Castellon Jorge - Estructuras de Datos


class dupla:
    def __init__(self) -> None:
        self.marca = False
        self.padre = -1
        self.l8: l8_queue = l8_queue()
    
    def reset(self):
        self.marca = False
        self.padre = -1

class grafo:
    def __init__(self, nvert) -> None:
        self.arr: list[dupla] = [dupla() for _ in range(nvert)]
    
    def insertar(self, origen, destino):
        self.arr[origen].l8.enqueue(destino)
    
    def _reset_duplas(self):
        for dup in self.arr:
            dup.reset()

    def dfs(self, origen, destino):
        encontre = 0
        self.arr[origen].marca = 1
        vert: dupla = self.arr[ origen ]
        i = 0
        num_vecinos = len( vert.l8 )
        while i < num_vecinos:
            adya = vert.l8[i]
            if not encontre and not self.arr[ adya ].marca:
                self.arr[adya].marca = 1
                self.arr[adya].padre = origen
                if adya == destino:
                    encontre = 1 
                else:
                    encontre, _ = self.dfs(adya, destino)
            i += 1

        return encontre, origen 


    def bfs(self, origen, destino):
        self._reset_duplas()
        encontre = 0
        self.arr[origen].marca = 1
        cola=l8_queue()
        cola.enqueue( origen )

        while not encontre and not cola.empty():
            curr_explorar_idx = cola.dequeue()
            vert: dupla = self.arr[curr_explorar_idx]
            adya_lista_index = 0
            adyacente_idx = vert.l8[adya_lista_index]
            num_adyacentes = len(vert.l8)
            while adya_lista_index < num_adyacentes and not encontre:
                if not self.arr[adyacente_idx].marca:
                    self.arr[adyacente_idx].padre = curr_explorar_idx
                    if adyacente_idx == destino:
                        encontre = 1
                    else:
                        self.arr[adyacente_idx].marca = 1
                        cola.enqueue( adyacente_idx )
                adya_lista_index += 1
                if adya_lista_index < num_adyacentes:
                    adyacente_idx = vert.l8[adya_lista_index]
        if encontre:
            print( self.mostrar_camino( destino ) )
        return encontre
    
    def mostrar_camino( self, origen: int ):
        camino = [origen]
        vert: dupla = self.arr[origen]
        while vert.padre != -1:
            camino.insert(0, vert.padre)
            vert = self.arr[ vert.padre ]
        return camino
    
    def __str__(self) -> str:
        fstr = ''
        for i, vert in enumerate(self.arr):
            fstr += (f'{i}, {str(vert.l8)}\n')
        return fstr
    def _finsert(self, verts, indexed_neighbors):
        for i, vert in enumerate(verts):
            for neighbor in indexed_neighbors[i]:
                self.insertar( vert, neighbor  )

   
def load_file( path ):
    path = path or 'C:\\Users\\juggb\\Downloads\\src\\DL\\tareas_structurasdd\\MinCut(3).txt'
    with open(path) as f:
        data = [line.split('\t') for line in f.readlines()]
        verts = [int(v[0]) for v in data]
        neighbors = [[int(i) for i in line[1:-1]] for line in data]
        _grafo = grafo( len(verts) + 1 )
        _grafo._finsert( verts, neighbors ) 
    return _grafo


# print(grafo_test.bfs_comp_traversal(1))
# print(grafo_test.dfs_comp_traversal_iter(1))
# print(grafo_test.dfs_comp_traversal_recurs(1))

menu_str = ['insert(o, a)',
'bfs(o, d)',
'dfs(o, d)',
'show traversal(o)',
'load file',
'show graph',
]
'''
Insertar_Grafo
Mostrar Camino
Búsqueda en Amplitud
Búsqueda en Profundidad
Leer archivo
'''
_grafo = grafo( 10 )
T=int
def console_loop():
    global _grafo
    while (inp:=input('{0}\n>> '.format( "\n".join(F'{i+1}. {v}' for i,v in enumerate(menu_str)) ))):
        try:
            opt=menu_str[int(inp)-1]
            print(f'{opt}>> ',end='')
        except ValueError:
            opt='error'
        if inp=='1':
            origin, dest = map(int, input().split(','))
            _grafo.insertar( origin, dest )
        if inp=='2':
            origin, dest = map(int, input().split(','))
            _grafo.bfs( origin, dest )
        if inp=='3':
            origin, dest = map(int, input().split(','))
            _grafo.dfs( origin, dest )
        if inp =='4':
            origin = int(input())
            print(_grafo.mostrar_camino( origin ))
        if inp =='5':
            _grafo = load_file( None )
        if inp == '6':
            print(_grafo)
        
        wait_key()
        clear()
console_loop()