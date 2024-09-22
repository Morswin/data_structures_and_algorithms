from lists.node_linked_list import NodeLinkedList, Node


def test_node_linked_list_default() -> None:
    nll = NodeLinkedList()
    assert nll is not None
    assert nll.head is None
    assert nll.length == 0
    
