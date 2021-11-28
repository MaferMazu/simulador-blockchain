"""Module of Blockchain"""
from models.identity import Identities
from models.block import Block


class Blockchain:
    """Blockchain Class."""

    def __init__(self):
        """Init."""
        blockchain = []
        utxo = []
        mempool = []


    def gen_genesis_block(self, identities: Identities):
        """Generates Block 0 with base transactions."""
        pass
