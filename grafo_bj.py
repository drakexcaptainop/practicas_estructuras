from tarea_lista_impl8_bj import l8_queue, l8_stack, clear, wait_key
from duo import duo, inf
from heap_min_bj import heap_min

class dupla:
    def __init__(self) -> None:
        self.marca = False
        self.padre = -1
        self.dist = inf
        self.l8: l8_queue[tuple[int, int]] = l8_queue()
    
    def reset(self):
        self.marca = False
        self.padre = -1
        self.dist = inf

class grafo:
    def __init__(self, nvert) -> None:
        self.arr: list[dupla] = [dupla() for _ in range(nvert)]
    
    def insertar(self, origen, destino, peso = 0):
        self.arr[origen].l8.enqueue( (destino, peso) )
    
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
            adya, _ = vert.l8[i]
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
            adyacente_idx, _ = vert.l8[adya_lista_index]
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
            for neighbor, weight in indexed_neighbors[i]:
                self.insertar( vert, neighbor, weight  )

    def bfs_comp_traversal(self, origin):
        self._reset_duplas()

        queue = l8_queue()
        queue.enqueue(origin)
        traverse_road = l8_stack()
        traverse_road.push(origin)
        self.arr[origin].marca = 1

        while not queue.empty():
            vert_index = queue.dequeue()
            vert: dupla = self.arr[vert_index]
            num_neighbors = len( vert.l8 )
            for ineighbor in range(num_neighbors):
                neighbor_index, _ = vert.l8[ineighbor]
                if not self.arr[neighbor_index].marca:
                    queue.enqueue( neighbor_index )
                    self.arr[neighbor_index].marca = 1
                    traverse_road.push( neighbor_index )
    
        return traverse_road


    def dfs_comp_traversal_iter(self, origin):
        self._reset_duplas()
        stack = l8_stack()
        traverse_road = l8_stack()
        traverse_road.push( origin )
        self.arr[origin].marca = 1
        stack.push(origin)

        while not stack.empty():
            vert_index = stack.pop()
            vert: dupla = self.arr[ vert_index ]
            vert_neighbors = vert.l8
            nneighbors = len(vert_neighbors)
            if nneighbors > 0:
                l8_index = 0
                while l8_index < nneighbors:
                    neighbor_index, _ = vert_neighbors[ l8_index ]
                    if not self.arr[ neighbor_index ].marca:
                        self.arr[ neighbor_index ].marca = 1
                        traverse_road.push( neighbor_index )
                        stack.push( vert_index )
                        stack.push( neighbor_index )
                        break
                    l8_index += 1
                
        return traverse_road


    def dfs_comp_traversal_recurs(self, origin, traverse_road=None):
        if traverse_road == None:
            self._reset_duplas()
            traverse_road = l8_stack()
            traverse_road.push( origin )
            self.arr[origin].marca = 1
        vert = self.arr[origin]
        nneighbors = len( vert.l8 )
        l8_index = 0
        while l8_index < nneighbors:
            neighbor_index, _ = vert.l8[ l8_index ]
            if not self.arr[neighbor_index].marca:
                traverse_road.push( neighbor_index )
                self.arr[neighbor_index].marca = 1
                self.dfs_comp_traversal_recurs( neighbor_index, traverse_road )
            l8_index += 1

        return traverse_road
    
    def dijkstra(self, origin):
        self._reset_duplas()

        n = len( self.arr )
        cola_p = heap_min( n*(n-1)//2 )
        self.arr[origin].dist = 0
        cola_p.insert( duo( origin, self.arr[ origin ].dist ) )

        while cola_p.last_leaf != 0:
            _duo: duo = cola_p.delete_top( )
            vert: dupla = self.arr[ _duo.vert ]

            num_neighbors = len(vert.l8)
            if not vert.marca and num_neighbors > 0:
                vert.marca = True
            #Verficar que tenga vertices adyacentes
                if num_neighbors > 0:
                    ady_l8_index = 0
                    while ady_l8_index < num_neighbors:
                        dest, weight = vert.l8[ ady_l8_index ]
                        ady: dupla = self.arr[ dest ]
                        if not ady.marca and vert.dist + weight < ady.dist:
                            ady.padre = _duo.vert
                            ady.dist = _duo.dist + weight
                            cola_p.insert( duo( dest, ady.dist ) )
                        ady_l8_index += 1





def load_file( path ):
    path = path or 'C:\\Users\\juggb\\Downloads\\src\\DL\\tareas_structurasdd\\MinCut(3).txt'
    with open(path) as f:
        data = [line.split('\t') for line in f.readlines()]
        verts = [int(v[0]) for v in data]
        neighbors = [[int(i) for i in line[1:-1]] for line in data]
        _grafo = grafo( len(verts) + 1 )
        _grafo._finsert( verts, neighbors ) 
    return _grafo

# grafo_test = load_file('')

# _, o = (grafo_test.dfs( 5, 128 ))
# print(grafo_test.mostrar_camino( 128 ))

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
            origin, dest, weight = map(int, input().split(','))
            _grafo.insertar( origin, dest, weight )
        if inp=='2':
            origin, dest = map(int, input().split(','))
            _grafo.dfs( origin, dest )
        if inp=='3':
            origin, dest = map(int, input().split(','))
            _grafo.dfs( origin, dest )
        if inp =='4':
            origin = int(input())
            _grafo.mostrar_camino( origin )
        if inp =='5':
            _grafo = load_file( None )
        if inp == '6':
            print(str(_grafo))
        
        wait_key()
        clear()
# console_loop()

_grafo._finsert( [1,2,3,4], [ [(2, 100), (3, 30)], [(3, 20)], [(4,10),(5,60)], [(5, 50), (2,15)] ] )
print(_grafo)
_grafo.dijkstra( 1 )
print(_grafo.mostrar_camino( 2 ))