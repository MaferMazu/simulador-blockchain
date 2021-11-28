"""Test Identity Class and Functions."""
from faker import Faker

from models.block import Block, BlockHeader, generate_merkle_root

faker = Faker()

def test_create_blockheader():
    """Test Create BlockHeader."""
    previous_hash = str(faker.sha256())
    difficulty = 0
    transactions = faker.words(7)
    blockheader = BlockHeader(previous_hash, difficulty, transactions)
    assert str(blockheader) == str(blockheader.to_dict())


def test_create_block():
    """Test Create Block."""
    previous_hash = str(faker.sha256())
    difficulty = 0
    transactions = faker.words(7)
    blockheader = BlockHeader(previous_hash, difficulty, transactions)
    block_hash = str(faker.sha256())
    miner = faker.first_name().lower()
    block = Block(blockheader, block_id=1,
        block_hash=block_hash, miner=miner,
        transactions=transactions
        )
    assert str(blockheader) == str(block.block_header)
    assert len(block.transactions) == 7
    assert block.block_size > 40


def test_object_merkle_tree():
    """Test merkle tree with list of objects."""
    b_1 = BlockHeader(str(faker.sha256()), 0, faker.words(2))
    b_2 = BlockHeader(str(faker.sha256()), 0, faker.words(3))
    b_3 = BlockHeader(str(faker.sha256()), 0, faker.words(5))
    blockheaders = [b_1, b_2, b_3]
    generate_merkle_root(blockheaders)
