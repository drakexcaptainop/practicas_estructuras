import os
clear = lambda: os.system('cls')
wait_key = lambda: input('...')

class node:
    def __init__(self, el, next=None, prev=None) -> None:
        self.next = next
        self.prev = prev
        self.el = el

class l8:
    def __init__(self) -> None:
        self.first = self.last = None
    
    def insert_first(self, x):
        if self.first is None:
            self.first = self.last = node( x )
        else:
            tmp = node( x, self.first )
            self.first.prev = tmp
            self.first = tmp
        
    def insert_last(self, x):
        if self.first is None:
            self.first = self.last = node( x )
        else:
            n = node( x, prev= self.last )
            self.last.next = n 
            self.last = n     
        

    def delete_first(self) -> bool:
        if self.first is None:
            res = False
        else:
            res = True
            self.first = self.first.next
            if self.first is None:
                self.last = None
            else:
                self.first.prev = None

        return res 

    def delete(self, x):
        deleted = False
        if self.first is None:
            return deleted
        else:
            if self.first.el == x:
                deleted = self.delete_first()
                # print(f'set true firsts {deleted = }')
            else:
                if self.last.el == x:
                    # print(f'{self.last.el = }')
                    deleted = self.delete_last()
                    # print(f'set true last {deleted = }')
                else:
                    cur = self.first
                    while cur != self.last and cur.el != x:
                        cur = cur.next
                    
                    if cur.el == x:
                        deleted = True
                        cur.prev.next = cur.next
                    # print(f'set true {deleted = }')
        # print(f'return {deleted = }')
        return deleted

        

    def delete_last(self) -> bool:
        if self.first is None:
            res = False
        else:
            if self.last == self.first:
                self.last = self.first = None
            else:
                self.last.prev.next = None
                self.last = self.last.prev

            res = True
        return res

    def delete_all(self):
        self.first = self.last = None

    def show(self):
        print(str(self))

    def __len__(self):
        counter = 0
        cur = self.first
        while cur != None:
            cur = cur.next
            counter += 1
        return counter

    def search(self, x):
        cur = self.first
        index = 0
        while cur != None:
            if cur.el == x:
                return index
            index += 1
            cur = cur.next
        return None
    
    def size(self):
        size = 0
        if self.first is None:
            return size
        cur = self.first
        while cur != None:
            cur = cur.next
            size += 1
        return size

    def sort(self):
        for _ in range(1, len(self)):
            for v in range(len(self) - 1):
                next = self[v + 1]
                cur = self[v]
                if cur > next:
                    self[v + 1], self[v] = cur, next
    
    def __str__(self) -> str:
        return '[' + ', '.join(str(v) for v in self) + ']'
    
    def __repr__(self) -> str:
        return str(self)

    def __iter__(self):
        cur = self.first
        while cur != None:
            yield cur.el 
            cur = cur.next

    def __setitem__(self, i, x):
        if self.first is None:
            raise IndexError('list is empty')
        counter = 0
        cur = self.first
        while cur != None:
            if counter == i:
                cur.el = x 
                return 
            cur = cur.next
            counter += 1
        
        raise IndexError( f'{ i } is out of range {0}-{counter - 1}' )
            
    #n1 - n2 - n3        
    def sort2(self):
        if self.first != None:
            outer = self.first
            while outer.next != None:
                icur = self.first
                while icur.next != None:
                    if icur.el > icur.next.el:
                        icur.next.el, icur.el = icur.el, icur.next.el
                    icur = icur.next
                outer = outer.next
            
    def __getitem__(self, i):
        if self.first is None:
            raise IndexError('list is empty')
        
        cur = self.first
        counter = 0
        while cur != None:
            if counter == i:
                return cur.el
            
            counter += 1 
            cur = cur.next
        
        raise IndexError( f'{ i } is out of range {0}-{counter - 1}' )
            
        
    @staticmethod
    def merge(l1: 'l8', l2: 'l8'):
        merged = l8()
        l1head = l1.first
        l2head = l2.first
        while l1head != None and l2head != None:
            merged.insert_last( l1head.el )
            merged.insert_last( l2head.el )
            l1head = l1head.next
            l2head = l2head.next
        
        while l1head != None:
            merged.insert_last( l1head.el )
            l1head = l1head.next
        
        while l2head != None:
            merged.insert_last( l2head.el )
            l2head = l2head.next
        
        return merged

    @staticmethod
    def from_array(it):
        l = l8()
        for i in it:
            l.insert_last(i)
        return l

class l8_queue(l8):
    def __init__(self) -> None:
        super().__init__()
    
    def enqueue(self, el):
        self.insert_last(el)
    
    def dequeue(self):
        if not self.empty():
            val = self[0]
            self.delete_first()
            return val 
    
    def empty(self):
        return self.first == None

class l8_stack(l8):
    def __init__(self) -> None:
        super().__init__()
    
    def push(self, el):
        self.insert_last(el)
    
    def pop(self):
        if not self.empty():
            el = self.last.el 
            self.delete_last()
            return el

    def empty(self):
        return self.first == None


menu_str = '''1. Insert First
2. Insert Last
3. Delete First
4. Delete Last
5. Show
6. Search
7. Sort (Burbuja)
8. Delete All
9. Search Pos []
'''

def console_loop():
    
    arr = l8()
    dtype = int 
    
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
            arr.sort2()
        elif inp=='8':
            arr.delete_all()
        elif inp=='9':
            index = int(input('index>>'))
            if index >= len(arr):
                print(f'index[{index}] is not in array range')
            else:
                print(arr[index])
            wait_key()

        clear()

#console_loop()


def merger_test():
    l1 = l8.from_array('abcde')
    l2 = l8.from_array('---')

    print(l8.merge(l1, l2))
