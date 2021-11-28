"""Class Network."""
from datetime import datetime

import click

from models.identity import Identities
from models.node import Node


class Network:
    """Class Network."""

    def __init__(self, identities: Identities=Identities()):
        """Init."""
        self.nodes = []
        self.identities = identities
        self.node_config = {"max_block_size": 512, "avgtime": 1, "difficulty": 1000}
        self.directory = None


    def __str__(self):
        """String method."""
        return str(self.to_dict())


    def add_log(self, node: Node, msg:click.Choice(['Presentacion', 'PresentacionAck', 'Transaccion',
                'TransaccionAck', 'TransaccionNueva', 'TransaccionNuevaAck', 'Bloque', 'BloqueAck']),
                extra:str=None, timestamp=datetime.now()):
        """Add logs in log dir."""
        if not self.directory:
            self.directory = "data/logs"
        
        with open(f"{self.directory}","a+") as log_file:
            log_file.write(f"Timestamp: {timestamp}\n")
            log_file.write(f"Mensaje: {msg}\n")
            if "Presentacion" in msg or not extra:
                log_file.write("\n")
            elif "Ack" in msg:
                log_file.write(f"Estado: {extra}\n")
            elif "Bloque" in msg:
                log_file.write(f"Bloque: {extra}\n")
            else:
                log_file.write(f"Transaccion: {extra}\n")


    def to_dict(self):
        """To dict method."""
        return {
            "nodes": [node.to_dict() for node in self.nodes],
            "identities": [str(identity) for identity in self.identities.identities],
            }


    def read_network_file(self, path):
        """Read Network file."""
        self.nodes = []
        with open(path, "r") as my_file:
            lines = my_file.readlines()
            nodes_num = int(lines[0])
            nodes = lines[1:nodes_num+1]
            connections_num = int(lines[nodes_num+1])
            connections = lines[nodes_num+2:]
            for elem in nodes:
                if elem:
                    token = elem.split(" ")
                    name = token[0]
                    node_id = int(name.replace("nodo", ""))
                    port = int(token[1])
                    identity = self.identities.search_by_name(name)
                    if identity:
                        node = Node(node_id=node_id, port=port)
                        self.nodes.append(node)

            for elem in connections:
                if elem:
                    token = elem.strip("\n").split(" ")
                    name1 = token[0]
                    name2 = token[1]
                    node1 = self.search_node_by_name(name1)
                    node2 = self.search_node_by_name(name2)

                    if node1 and node2:
                        node1.adj.add(node2)
                        node2.adj.add(node1)


    def search_node_by_name(self, name):
        """Search node by name."""
        for elem in self.nodes:
            if elem.name == name:
                return elem
        return None


    def read_node_config(self, path):
        """Read the config file."""
        with open(path,"r") as my_file:
            lines = my_file.readlines()
            max_size = int(lines[0].split(":")[1])
            avg_time = int(lines[1].split(":")[1])
            difficulty = int(lines[2].split(":")[1])
            self.node_config = {
                "max_block_size": max_size,
                "avgtime": avg_time,
                "difficulty": difficulty}

# network = Network()
# network.identities.gen_x_identities(5)
# network.identities.gen_x_nodes(5)
# network.read_network_file("file_examples/network_file.txt")
# assert len(network.identities) == 10
# assert len(network.nodes) == 5
# nodo1 = network.search_node_by_name("nodo1")
# nodo2 = network.search_node_by_name("nodo2")
# nodo3 = network.search_node_by_name("nodo3")
# assert len(nodo1.adj) == 1
# assert len(nodo2.adj) == 2
# assert len(nodo3.adj) == 3
