"""Class Node"""
import socket
from models.blockchain import Blockchain
from models.identity import Identities

class Node:
    """class Node."""

    def __init__(self, node_id, port=None, ledger=Blockchain()):
        """Init."""
        self.node_id = node_id
        self.port = port
        self.ledger = ledger
        self.name = f"nodo{node_id}"
        self.socket = None
        self.adj = {}

    def __str__(self):
        """String method."""
        return str(self.to_dict())

    def to_dict(self):
        """Convert in dict."""
        return {"name": self.name, "port": self.port}

    def _init_socket(self):
        if self._is_port_in_use():
            self._stop_socket()

    def _is_port_in_use(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', self.port)) == 0

    def _stop_socket(self):
        if self.socket:
            self.socket.close()


def run_node(name):
    """Prende un nodo y pone a escuchar y a enviar mensajes."""
    print(name)

