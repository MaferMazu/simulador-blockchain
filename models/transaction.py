"""Class about Transaction"""
from time import sleep
from datetime import datetime

class Transaction:
    """Transaction Class."""

    def __init__(self, sender, receiver, inputs, outputs):
        """Create Transaction."""
        
        self.sender = sender
        self.receiver = receiver
        self.timestamp = datetime.now()
        self.inputs = inputs
        self.outputs = outputs
        # Crea una transacción
        # hash
        # de quien
        # para quien
        # timestamp
        # monto en satoshis
        # fee

class Transactions:
    """Class with several transactions."""

    def __init__(self):
        """Init function."""
        self.mempool = []
        self.utxo = []
        self.config = {
                "frequency": 2, #Transactions per minute
                "min_input": 1,
                "max_input": 2,
                "min_output": 1,
                "max_output": 2,
                "nodes": set(),
                }


    def read_transaction_config(self, path):
        """Read the config file."""
        with open(path,"r") as my_file:
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

    def gen_random_transactions(self, count=20):
        """Generate random transactions."""
        secs = 60/self.config["frequency"]
        while count:
            sleep(secs)

    def gen_transac(self, sender, receiver, inputs, outputs):
        if self.correct_input(inputs):
            transaction = Transaction(sender, receiver, inputs, outputs)
            return transaction
        return None

    def correct_input(inputs):
        return True

