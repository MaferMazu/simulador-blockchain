"""File with common vars."""

import pickle
from pathlib import Path
from hashlib import sha256

location = Path(__file__).absolute().parent.parent

def export_data(object_name, my_object):
    """Save data to a data dir."""
    with open(f"data/{object_name}.pkl","wb") as my_file:
        pickle.dump(my_object, my_file)

def import_data(object_name):
    """Extract data from data dir."""
    with open(f"data/{object_name}.pkl","rb") as my_file:
        return pickle.load(my_file)

def create_hash(my_string):
    return sha256(my_string.encode('utf-8')).hexdigest()
