from tarea_lista_impl8_bj import l8, wait_key
#Barahona Castellon Jorge - Estructuras de datos

class node:
    def __init__(self, char, is_str_end=False) -> None:
        self.char = char
        self.children: node = None
        self.left: node = None
        self.is_str_end=is_str_end

class trie:
    def __init__(self) -> None:
        self.head=node('')

    def _insert(self, chars: str, _node: node):
        if chars=='':
            _node.is_str_end = True
            return True
        next_node=None
        if _node.children == None:
            _node.children = node( chars[0] )
            next_node = _node.children
        else:
            cur_child : node = _node.children
            while cur_child.left != None and cur_child.char != chars[0]:
                cur_child = cur_child.left
            if cur_child.char != chars[0]:
                cur_child.left = node( chars[0] )
                next_node = cur_child.left
            else:
                next_node = cur_child
        return self._insert( chars[1:], next_node )

    def _search_subtree( self, chars, _node: node ):
        if chars=='':
            return _node
        if _node is None:
            return None
        else:
            cur_child = _node.children
            ret_node = None
            if cur_child is not None:
                while cur_child.left != None and cur_child.char != chars[0]:
                    cur_child = cur_child.left
                if len(chars) == 1:
                    if cur_child.char == chars[0]:
                        ret_node = cur_child
                elif len(chars) > 1:
                    ret_node = self._search_subtree( chars[1:], cur_child )
                else:
                    ret_node = _node
            
            return ret_node
        
    def concat_str_recurs(self, _node: node, cur_prefix: str, cache_vec: l8 = None):
        if  _node.children is None:
            cache_vec.insert_last( cur_prefix )
        else:
            cur_child = _node.children
            while cur_child != None:
                self.concat_str_recurs( cur_child, cur_prefix+cur_child.char, cache_vec )    
                cur_child = cur_child.left
            if _node.is_str_end:
                cache_vec.insert_last( cur_prefix )

    def search_str( self, chars ):
        _search_node = self._search_subtree( chars, self.head )
        if _search_node is not None:
            vec_strs_results = l8()
            self.concat_str_recurs( _search_node,chars,vec_strs_results )
            return vec_strs_results
        else:
            return None
    
    def insert(self, chars):
        return self._insert( chars, self.head )

    def _delete(self, chars, _node: node):
        if _node != None and _node.is_str_end == True and chars == '':
            return True

        if not _node.is_str_end and chars=='':
            return False

        cur_node = _node.children
        prev_ref = _node
        while cur_node != None and cur_node.char != chars[0]:
            prev_ref = cur_node
            cur_node = cur_node.left
        
        if cur_node != None:
            has_been_found = self._delete( chars[1:], cur_node )
            if has_been_found:
                if prev_ref == _node:
                    _node.children = _node.children.left
                    if not _node.is_str_end:
                        return True if _node.children is None else False
                else:
                    if cur_node.children != None:
                        cur_node.is_str_end = False
                    else:
                        prev_ref.left = cur_node.left 
        else:
            return False
        

t = trie( )
t.insert('maria')
t.insert('mariano')
t.insert('maestra')
t.insert('mario')
t.insert('ma')



t._delete( 'maestra', t.head )

t._delete( 'mario', t.head )
print(t.search_str('ma'))









menu_str='''
1. Insert
2. Search
'''
def console_loop():
    while (inp:=input(f'{menu_str}\n>> ')):
        if inp=='1':
            arg=input('insert>> ')
            t.insert( arg )

        if inp=='2':
            arg=input('search>> ')
            res= t.search_str( arg )
            print(res or '[]')
            wait_key()
        
        if inp=='3':
            arg=input('delete>> ')
            t._delete( arg, t.head )

# console_loop(  )