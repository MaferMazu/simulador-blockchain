"""Class about Transaction"""
import random
from datetime import datetime

from models.common import create_hash
from models.identity import Identities


class Output:
    """Class Output."""
    # pylint: disable=too-few-public-methods
    def __init__(self, owner, satoshis):
        """Init."""
        self.owner = owner
        self.hash = create_hash(f"{owner.name} {satoshis}")
        self.satoshis = satoshis

    def __str__(self):
        """String."""
        return self.hash


class Transaction:
    """Transaction Class."""
    # pylint: disable=too-few-public-methods
    def __init__(self, inputs, outputs, node=None):
        """Create Transaction."""

        self.timestamp = datetime.now()
        self.inputs = inputs
        self.outputs = outputs
        self.node = node
        self.hash = create_hash(f"{str(node)} {str(inputs)} {str(outputs)} {str(self.timestamp)}")

    def get_fee(self):
        """Get fee."""
        total_amount_input = 0
        for inp in self.inputs:
            total_amount_input += inp.satoshis
        total_amount_output = 0
        for out in self.outputs:
            total_amount_output += out.satoshis

        return total_amount_input - total_amount_output


class Transactions:
    """Class with several transactions."""

    def __init__(self):
        """Init function."""
        self.mempool_confirmed = []
        self.transactions_not_confirmed = []
        self.utxo = []
        self.config = {
                "frequency": 2,
                "min_input": 1,
                "max_input": 2,
                "min_output": 1,
                "max_output": 2,
                "nodes": set(),
                }

    def read_transaction_config(self, path):
        """Read the config file."""
        with open(path,"r", encoding='utf-8') as my_file:
            lines = my_file.readlines()
            frequency = int(lines[0].split(":")[1])
            min_input = int(lines[1].split(":")[1])
            max_input = int(lines[2].split(":")[1])
            min_output = int(lines[3].split(":")[1])
            max_output = int(lines[4].split(":")[1])
            self.config = {
                "frequency": frequency,
                "min_input": min_input,
                "max_input": max_input,
                "min_output": min_output,
                "max_output": max_output,
                }

    def gen_random_transaction(self, identities: Identities):
        """Generate random transaction."""
        random_inputs = self.select_random_inputs()
        random_outputs = self.create_random_outputs(identities, random_inputs)
        random_node = random.choice(list(self.config["nodes"]))
        transaction = self.gen_simple_transac(random_inputs, random_outputs, random_node)
        self.transactions_not_confirmed.append(transaction)
        return transaction

    def select_random_inputs(self):
        """Select random inputs."""
        # pylint: disable=line-too-long
        how_much_inputs = 50
        top = len(self.utxo) if len(self.utxo) < self.config["max_input"] else self.config["max_input"]
        how_much_inputs = random.randrange(self.config["min_input"], top + 1)

        random_inputs = random.sample(self.utxo, how_much_inputs)
        return random_inputs

    def create_random_outputs(self, identities, random_inputs):
        """Create random outputs."""
        how_much_satoshis = calculate_satoshis(random_inputs)
        fee = random.randrange(50, 100)
        satoshis_to_share = how_much_satoshis - fee
        outputs = []
        times = 0
        while satoshis_to_share > 0 and times < self.config["max_output"]:
            satoshis = random.randrange(1, satoshis_to_share)
            identity = random.choice(identities.identities)
            output = Output(identity, satoshis)
            satoshis_to_share -= satoshis
            times += 1
            outputs.append(output)
        if satoshis_to_share > 0:
            identity = random.choice(identities.identities)
            output = Output(identity, satoshis_to_share)
            outputs.append(output)
        return outputs

    def gen_simple_transac(self, inputs, outputs, node=None):
        """Gen simple transaction."""
        if correct_input():
            transaction = Transaction(inputs, outputs, node)
            self.process_inputs(inputs)
            self.process_outputs(outputs)
            return transaction
        return None

    def process_inputs(self, inputs):
        """Process inputs."""
        for elem in inputs:
            self.utxo.remove(elem)

    def process_outputs(self, outputs):
        """Process outputs."""
        for elem in outputs:
            self.utxo.append(elem)


def calculate_satoshis(my_list_of_outputs):
    """Calculate satoshis."""
    result = 0
    for output in my_list_of_outputs:
        result += output.satoshis
    return result


def correct_input():
    """Correct input."""
    return True
