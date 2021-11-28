"""Class Block"""
from datetime import datetime
from sys import getsizeof

from merkletools import MerkleTools


class BlockHeader:
    """BlockHeader Class."""

    def __init__(self, previous_hash, difficulty, transactions):
        """Init."""
        self.previous_hash = previous_hash
        self.timestamp = datetime.now()
        self.difficulty = difficulty
        self.merkle_root = generate_merkle_root(transactions)


    def __str__(self):
        """String function."""
        return str(self.to_dict())


    def to_dict(self):
        """Transform to dict."""
        return {
            "previous_hash": self.previous_hash,
            "timestamp": str(self.timestamp),
            "difficulty": self.difficulty,
            "merkle_root": self.merkle_root,
            }


class Block:
    """Block Class."""
    # pylint: disable=too-many-arguments
    def __init__(self, block_header: BlockHeader, block_id, block_hash, miner, transactions):
        """Init function."""
        self.block_id = block_id
        self.hash = block_hash
        self.miner = miner
        self.transactions = transactions
        self.block_header = block_header
        self.block_size = self._calculate_block_size()


    def _calculate_block_size(self):
        """Calculate block size."""
        return getsizeof(self)


    def __str__(self):
        """String function."""
        return str(self.to_dict())


    def to_dict(self):
        """Transform to dict."""
        return {
            "block_id": self.block_id,
            "hash": self.hash,
            "miner": self.miner,
            "transactions": self.transactions,
            "block_header": self.block_header.to_dict(),
            "block_size": self.block_size,
        }


def generate_merkle_root(transactions):
    """Generate Merkle Root."""

    merkle = MerkleTools()
    for transaction in transactions:
        merkle.add_leaf(str(transaction), True)
    merkle.make_tree()
    if merkle.is_ready:
        return merkle.get_merkle_root()
    return None
