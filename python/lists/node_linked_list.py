from typing import Union


class Node:
    # value: int
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
    head: Union[Node, None] = None
    # head: Node|None
    length: int  = 0
    # length: int

    def __init__(self):
        head = None
        length = 0


class NodeLinedListWithLoop:
    pass


class NodeDoubleLinkedList:
    pass
