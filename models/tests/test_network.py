"""Test Identity Class and Functions."""
from models.network import Network


def test_empty_network():
    """Test creation of empty network."""
    network = Network()
    assert network is not None


def test_network():
    """Test creation of network."""
    network = Network()
    network.identities.gen_x_identities(5)
    network.gen_x_nodes(3)
    network.create_linear_network()
    assert len(network.identities) == 8
    assert len(network.connections) == 2
