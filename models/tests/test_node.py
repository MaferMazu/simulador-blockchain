"""Test Node Class and Functions."""
from models.node import Node


def test_node():
    """Test creation of node."""
    node = Node(1, 9000)
    assert node.name == "nodo1"
    assert str(node) == str({"name": "nodo1", "port": 9000})
