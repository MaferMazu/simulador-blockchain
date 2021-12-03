"""Test Transaction Class and Functions."""

from models.common import create_hash
from models.identity import Identities, Identity
from models.node import Node
from models.transaction import Output, Transaction, Transactions, calculate_satoshis


def test_output():
    """Test."""
    owner = Identity("test", "email@example.com")
    satoshis = 1000
    output = Output(owner, satoshis)
    assert str(output) == create_hash(f"{owner.name} {satoshis}")


def test_get_fee():
    """Test."""
    transaction = Transaction([], [])
    assert transaction.get_fee() == 0


def test_read_transaction_config():
    """Test."""
    transactions = Transactions()
    transactions.read_transaction_config("examples/file_examples/transac_config.txt")
    assert transactions.config["frequency"] == 1
    assert transactions.config["min_input"] == 1
    assert transactions.config["min_output"] == 1
    assert transactions.config["max_input"] == 3
    assert transactions.config["max_output"] == 3


def test_gen_random_transaction():
    """Test."""
    identities = Identities()
    identities.gen_x_identities(5)
    identities.gen_x_nodes(1)
    node = Node(1, 9110)
    transactions = Transactions()
    transactions.config["nodes"].add(node)
    for elem in identities.identities:
        output = Output(elem, 10000000)
        transactions.utxo.append(output)
    transactions.gen_random_transaction(identities)

    assert len(transactions.transactions_not_confirmed) == 1


def test_calculate_satoshis():
    """Test."""
    identities = Identities()
    identities.gen_x_identities(5)
    outputs = []
    for elem in identities.identities:
        output = Output(elem, 10000000)
        outputs.append(output)
    assert calculate_satoshis(outputs) == 50000000
