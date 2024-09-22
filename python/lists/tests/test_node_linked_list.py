from lists.node_linked_list import NodeLinkedList, Node


def test_node_linked_list_default() -> None:
    nll = NodeLinkedList()
    assert nll is not None
    assert nll.head is None
    assert nll.length == 0

def test_list_is_empty() -> None:
    nll = NodeLinkedList()
    assert nll.is_empty() == True

def test_insert_value_at_the_beginning() -> None:
    nll = NodeLinkedList()
    nll.insert_front(10)
    assert nll.head is not None
    assert nll.length == 1
    assert nll.head.value == 10
