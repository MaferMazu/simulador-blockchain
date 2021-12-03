"""File with common vars."""
from hashlib import sha256
from math import log
from pathlib import Path

import click
import dill as pickle

location = Path(__file__).absolute().parent.parent
MAX_NONCE = 2 ** 32  # 4 billion


def export_data(object_name, my_object):
    """Save data to a data dir."""
    with open(f"data/{object_name}.pkl", "wb") as my_file:
        pickle.dump(my_object, my_file)


def import_data(object_name):
    """Extract data from data dir."""
    with open(f"data/{object_name}.pkl", "rb") as my_file:
        return pickle.load(my_file)


def create_hash(my_string):
    """Create hash."""
    return sha256(my_string.encode('utf-8')).hexdigest()


def proof_of_work(header, difficulty: int):
    """PoW from Mastering Bitcoin."""
    # calculate the difficulty target
    difficulty_bits = log(difficulty, 2)
    target = 2 ** (256 - difficulty_bits)
    click.echo(f"Target {target}")

    for nonce in range(MAX_NONCE):
        hash_result = sha256((str(header)+str(nonce)).encode('utf-8')).hexdigest()

        # check if this is a valid result, below the target
        try:
            if int(hash_result, 16) < target:
                click.echo(f"Success with nonce {nonce}")
                click.echo(f"Hash is {hash_result}")

                return (hash_result, nonce)
        except ValueError:
            pass

    click.echo(f"Failed after {nonce} (max_nonce) tries")
    return nonce, hash_result
