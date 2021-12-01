"""Test Identity Class and Functions."""
from models.network import Network

from pathlib import Path

location = Path(__file__).absolute().parent.parent


def test_empty_network():
    """Test creation of empty network."""
    del_network()
    network = Network()
    assert network is not None


def test_read_network_file():
    """Read network file."""
    del_network()
    network = Network()
    network.identities.gen_x_identities(5)
    network.identities.gen_x_nodes(5)
    network.read_network_file("examples/file_examples/network_file.txt")
    print(len(network.identities))
    assert len(network.identities) == 10
    assert len(network.nodes) == 5
    nodo1 = network.search_node_by_name("nodo1")
    nodo2 = network.search_node_by_name("nodo2")
    nodo3 = network.search_node_by_name("nodo3")
    nodo1.stop()
    nodo2.stop()
    nodo3.stop()
    assert len(nodo1.adj) == 1
    assert len(nodo2.adj) == 2
    assert len(nodo3.adj) == 3


def test_read_node_config():
    """Test read node config."""
    del_network()
    network = Network()
    network.read_node_config("examples/file_examples/node_config.txt")
    assert network.node_config["max_block_size"] == 513
    assert network.node_config["avgtime"] == 3
    assert network.node_config["difficulty"] == 1001


def test_read_node_file_for_transactions():
    """Tes for read_node_file_for_transactions function."""
    del_network()
    network = Network()
    network.identities.gen_x_identities(5)
    network.identities.gen_x_nodes(5)
    network.read_network_file("examples/file_examples/other_network_file.txt")
    print(len(network.identities))
    nodo1 = network.search_node_by_name("nodo1")
    nodo2 = network.search_node_by_name("nodo2")
    nodo3 = network.search_node_by_name("nodo3")
    nodo1.stop()
    nodo2.stop()
    nodo3.stop()
    assert len(nodo1.adj) == 1
    assert len(nodo2.adj) == 2
    assert len(nodo3.adj) == 3
    network.read_node_file_for_transactions("examples/file_examples/other_node_file.txt")
    set_of_names = set([node.name for node in network.transactions.config["nodes"]])
    assert set_of_names == {"nodo1","nodo2","nodo4","nodo5"}


def del_network():
    try:
        del network
    except:
        pass
