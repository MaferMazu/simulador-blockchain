"""Class Node"""
import click
import socket
from p2pnetwork.node import Node as P2PNode

from models.common import export_data, import_data

class MyP2PNode(P2PNode):

    def __init__(self, host, port, id=None, callback=None, max_connections=0):
        super(MyP2PNode, self).__init__(host, port, id, callback, max_connections)

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


class Node():
    """Class Node."""

    def __init__(self, node_id, port, host="127.0.0.1",
                callback=None, max_connections=0,
                blockchain=[], is_on=False,
                identity=None):
        """ Init function."""

        self.node_id = node_id
        self.port = port
        self.blockchain = blockchain
        self.name = f"nodo{node_id}"
        self.adj = set()
        self.is_on = is_on
        self.identity = identity
        self.node = {"node":None}
        self.create_socket(host, port, node_id, callback, max_connections)

    def create_socket(self,host, port, node_id, callback, max_connections):
        """Create socket."""
        self.node["node"]=MyP2PNode(host, port, node_id, callback, max_connections)

    def propagation(self, nodes, data):
        # import pudb; pu.db
        neightbors = list(self.adj)
        to_propagate = [elem for elem in neightbors if elem in nodes and elem.is_on]
        for elem in to_propagate:
            nodes.remove(elem)
            node_connection = self.get_node_connection(elem)
            if not node_connection:
                self.node.connect_with_node(elem.host, elem.port)
                print(f"Se conocieron {self.name} y {elem.name}")
                node_connection = self.get_node_connection(elem)
            self.node.send_to_node(node_connection, data)
            elem.propagation(nodes,data)

    def start(self):
        network = import_data("network")
        self.node.start()
        self.is_on = True
        export_data("network", network)

    def stop(self):
        network = import_data("network")
        self.node.stop()
        self.is_on = False
        export_data("network", network)

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

