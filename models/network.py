"""Class Network."""
from datetime import datetime
from time import sleep

import click

from models.block import Block, BlockHeader
from models.identity import Identities
from models.node import Node
from models.transaction import Output, Transactions


class Network:
    """Class Network."""

    def __init__(self, identities:Identities=Identities(), transactions:Transactions=Transactions()):
        """Init."""
        self.nodes = []
        self.identities = identities
        self.node_config = {"max_block_size": 512, "avgtime": 1, "difficulty": 1000}
        self.directory = None
        self.transactions = transactions


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

    
    def read_node_file_for_transactions(self, path):
        """Read nodes file."""
        self.transactions.config["nodes"]=set()
        with open(path, "r") as my_file:
            lines = my_file.readlines()
            nodes_num = int(lines[0])
            nodes = lines[1:nodes_num+1]
            for elem in nodes:
                if elem:
                    token = elem.split(" ")
                    name = token[0]
                    node = self.search_node_by_name(name)
                    if node:
                        self.transactions.config["nodes"].add(node)


    def propagation(self, node, data):
        """Propagate info for nodes."""
        nodes = self.nodes.copy()
        nodes.remove(node)
        node.propagation(nodes, data)


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

    def gen_block_0(self):
        """Generates Block 0 with base transactions."""
        outputs = []
        for elem in network.identities.identities:
            output = Output(elem, 10000000)

        transaction = network.transactions.gen_simple_transac(None, outputs=outputs)
        block_header = BlockHeader(None, 0, [transaction])
        block = Block(block_header, 0, block_hash, None, [transaction])

    def gen_random_transactions(self, identities:Identities, count=20):
        """Generate random transactions."""
        secs = 60/self.transactions.config["frequency"]
        while count:
            sleep(secs)
            transaction = self.transactions.gen_random_transaction(self.identities, count)
            msg = f"TransaccionNueva\n{transaction.node.name}\n{str(transaction)}"
            self.propagate(transaction.node,msg)




# network = Network()
# network.identities.gen_x_identities(5)
# network.identities.gen_x_nodes(5)
# # import pudb; pu.db
# network.read_network_file("examples/file_examples/other_network_file.txt")
# nodo1 = network.search_node_by_name("nodo1")
# nodo2 = network.search_node_by_name("nodo2")
# nodo3 = network.search_node_by_name("nodo3")
# nodo1.start()
# nodo2.start()
# nodo3.start()
# nodo2.connect_with_node(nodo1.host, int(nodo1.port))
# nodo3.connect_with_node(nodo1.host, int(nodo1.port))

# network.read_node_file_for_transactions("examples/file_examples/other_node_file.txt")

# network.propagation(nodo2, "hola")

# nodo1.stop()
# nodo2.stop()
# nodo3.stop()
