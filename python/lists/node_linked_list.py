from typing import Union


class Node:
    ''' Node class.
        
    '''
    value = 0
    # value: int
    next_node = None
    # next_node: Union[type(self), None]

    def __init__(self, value, next_node):
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
                _current_node: Node = self.head
                _i: int = 0
                while _current_node is not None:
                    if _i == index:
                        # Let's insert this thing
                        _new_node = Node(value, _current_node.next_node)
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

    def insert_back(self, value: int) -> None:
        ''' Insert value at the very back of the list.
            
        '''
        if self.is_empty():
            self.head = Node(value)
        else:
            _current_node: Node = self.head
            while True:
                if _current_node is None:
                    break
                if _current_node.next_node is None:
                    _current_node.next_node = Node(value)
                    break
                _current_node = _current_node.next_node


class NodeLinedListWithLoop:
    ''' Node-based Linked List, that loops over.
        
    '''
    pass


class NodeDoubleLinkedList:
    ''' Node-based Dobule Linked List.
        
    '''
    pass
