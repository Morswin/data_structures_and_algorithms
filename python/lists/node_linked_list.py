from typing import Union, Self


class Node:
    ''' Node class.
        
    '''
    value: int
    # value: int
    next_node: Union[Self, None]
    # next_node: Union[type(self), None]

    def __init__(self, value=0, next_node=None):
        if value is not None:
            self.value = value
        else:
            self.value = 0

        if next_node is not None:
            self.next_node = next_node
        else:
            self.next_node = None


class NodeLinkedList:
    ''' Node-based Linked List.
        
    '''
    head: Union[Node, None] = None
    # head: Node|None
    length: int  = 0
    # length: int

    def __init__(self):
        head = None
        length = 0

    def is_empty(self) -> bool:
        ''' Does the list contain any values?
            
        '''
        if self.head is None:
            return True
        return False

    def insert(self, value: int, index: int) -> None:
        ''' Insert a value at given index.
            
        '''
        if self.is_empty():
            self.head = Node(value)
            self.length += 1
        else:
            # Is this index valid?
            if index < 0:
                raise IndexError("You've tried to insert a value to a negative index, which isn't implemented in this type of list.")
            elif self.length < index:
                raise IndexError("You've tried to insert a value to a nonexistent index.")
            else:
                # Right index has been found.
                # Now to insert the value successfully
                if self.head is None:
                    return None
                _current_node: Union[Node, None] = self.head
                _i: int = 0
                while _current_node is not None:
                    if _current_node is None:
                        return None
                    if _i == index:
                        # Let's insert this thing
                        _new_node: Union[Node, None] = Node(value, _current_node.next_node)
                        _current_node.next_node = _new_node
                        break
                    _i += 1
                    _current_node = _current_node.next_node
            

    def insert_front(self, value: int) -> None:
        ''' Insert value at the very front of the list.
            
        '''
        if self.is_empty():
            self.head = Node(value)
        else:
            _new_node = Node(value, self.head)
            self.head = _new_node
        self.length += 1

    def insert_last(self, value: int) -> None:
        ''' Insert value at the very back of the list.
            
        '''
        if self.is_empty():
            self.head = Node(value)
        else:
            if self.head is None:
                return None
            _current_node: Node = self.head
            while True:
                if _current_node is None:
                    return None
                if _current_node.next_node is None:
                    _current_node.next_node = Node(value)
                    break
                _current_node = _current_node.next_node
        self.length += 1

    def update(self, value: int, index: int):
        ''' Update a value at given index.
            
        '''
        if self.is_empty():
            raise IndexError("You've tried to update a value in an empty list.")
        elif self.length <= index:
            raise IndexError("You've tried to update a value at index that doesn't exist")
        elif index < 0:
            raise IndexError("You've tried to update a value at negative index which is not supported in this type of list.")
        else:
            if self.head is None:
                return None
            _current_node: Node = self.head
            _i: int = 0
            while True:
                if _current_node is None:
                    return None
                if _current_node.next_node is None:
                    return None
                if _i == index:
                    _current_node.value = value
                    break
                _i += 1
                _current_node = _current_node.next_node
    
    def delete(self, index: int) -> Union[int, None]:
        ''' Delete value at specific index.
            
        '''
        if not self.is_empty():
            if index < 0:
                raise IndexError("You've tried to delete negative index, which is not supported in this type of list.")
            elif index >= self.length:
                raise IndexError("You've tried tp delete index outside of the list.")
            else:
                if index == 0:
                    return self.delete_first()
                elif index == self.length - 1:
                    return self.delete_last()
                else:
                    if self.head is None:
                        return None
                    _current_node: Node = self.head
                    _previous_node: Node = self.head
                    _i: int = 0
                    while True:
                        if _current_node is None:
                            return None
                        if _current_node.next_node is None:
                            return None
                        if _i == index:
                            _value: int = _current_node.value
                            _previous_node.next_node = _current_node.next_node
                            self.length -= 1
                            return _value
                        _previous_node = _current_node
                        _current_node = _current_node.next_node
        return None

    def delete_first(self) -> Union[int, None]:
        ''' Delete first node.
            
        '''
        if not self.is_empty():
            if self.head is None:
                return None
            _value: int = self.head.value
            if self.head.next_node is None:
                self.head = None
                self.length -= 1
                return _value
            else:
                self.head = self.head.next_node
                self.length -= 1
                return _value
        return None

    def delete_last(self) -> Union[int, None]:
        ''' Delete last node.
            
        '''
        if not self.is_empty() and self.head is not None:
            _current_node: Node = self.head
            while True:
                if _current_node is None:
                    return None
                if _current_node.next_node is None:
                    return None 
                if _current_node.next_node.next_node is None:
                    if _current_node.next_node is None:
                        return None
                    _value: int = _current_node.next_node.value
                    _current_node.next_node = None
                    self.length -= 1
                    return _value
                _current_node = _current_node.next_node
        return None

    def get_at(self, index: int) -> Union[int, None]:
        ''' Get the value at given index.
            
        '''
        if index < 0:
            raise IndexError("You've tried to get value from a negative index which is not supported in this data structure")
        if index >= self.length:
            raise IndexError("You've tried to get value at an index outside of this list's length")
        if not self.is_empty() and self.head is not None:
            if index == 0:
                return self.get_first()
            elif index == self.length - 1:
                return self.get_last()
            else:
                _i: int = 0
                _current_node: Union[Node, None] = self.head
                while True:
                    if _current_node is None:
                        return None
                    if _i == index:
                        return _current_node.value
                    _i += 1
                    _current_node = _current_node.next_node
        return None

    def get_first(self) -> Union[int, None]:
        ''' Get the first value.
            
        '''
        if not self.is_empty() and self.head is not None:
            return self.head.value
        return None

    def get_last(self) -> Union[int, None]:
        ''' Get the last value.
            
        '''
        if not self.is_empty() and self.head is not None:
            _current_node: Union[Node, None] = self.head
            while True:
                if _current_node is None:
                    return None
                if _current_node.next_node is None:
                    return _current_node.value
                _current_node = _current_node.next_node
        return None


class NodeLinedListWithLoop:
    ''' Node-based Linked List, that loops over.
        
    '''
    pass


class NodeDoubleLinkedList:
    ''' Node-based Dobule Linked List.
        
    '''
    pass
