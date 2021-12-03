"""Class Node"""
import click
import socket
from p2pnetwork.node import Node as P2PNode

from models.blockchain import Blockchain


class Node(P2PNode):
    """Class Node."""

    def __init__(self, node_id, port, host="127.0.0.1",
                callback=None, max_connections=0,
                ledger=Blockchain(), is_on=False,
                identity=None):
        """ Init function."""
        super(Node, self).__init__(host, port, node_id,
                                    callback, max_connections)
        self.node_id = node_id
        self.port = port
        self.ledger = ledger
        self.name = f"nodo{node_id}"
        self.adj = set()
        self.is_on = is_on
        self.identity = identity

    def propagation(self, nodes, data):
        # import pudb; pu.db
        neightbors = list(self.adj)
        to_propagate = [elem for elem in neightbors if elem in nodes and elem.is_on]
        for elem in to_propagate:
            nodes.remove(elem)
            node_connection = self.get_node_connection(elem)
            if not node_connection:
                self.connect_with_node(elem.host, elem.port)
                print(f"Se conocieron {self.name} y {elem.name}")
                node_connection = self.get_node_connection(elem)
            self.send_to_node(node_connection, data)
            elem.propagation(nodes,data)

    def start(self):
        super(Node, self).start()
        self.is_on = True

    def stop(self):
        super(Node, self).stop()
        self.is_on = False

    def get_node_connection(self, node):
        for elem in self.nodes_outbound:
            if elem.id == node.id:
                return elem
        for elem in self.nodes_inbound:
            if elem.id == node.id:
                return elem
        return None

    def node_message(self, node, data):
        click.echo(f"Se envió un mensaje desde {nodo.name}")    

    def __str__(self):
        """String method."""
        return str(self.to_dict())

    def to_dict(self):
        """Convert in dict."""
        return {"name": self.name, "port": self.port}

    def outbound_node_connected(self, node):
        print("outbound_node_connected (" + self.id + "): " + node.id)
        
    def inbound_node_connected(self, node):
        print("inbound_node_connected: (" + self.id + "): " + node.id)

    def inbound_node_disconnected(self, node):
        print("inbound_node_disconnected: (" + self.id + "): " + node.id)

    def outbound_node_disconnected(self, node):
        print("outbound_node_disconnected: (" + self.id + "): " + node.id)

    def node_message(self, node, data):
        print("node_message (" + self.id + ") from " + node.id + ": " + str(data))
        
    def node_disconnect_with_outbound_node(self, node):
        print("node wants to disconnect with oher outbound node: (" + self.id + "): " + node.id)
        
    def node_request_to_stop(self):
        print("node is requested to stop (" + self.id + "): ")

