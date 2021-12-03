"""Class Node"""
import click
from p2pnetwork.node import Node as P2PNode


class Node(P2PNode):
    """Class Node."""
     # pylint: disable=too-many-arguments
    def __init__(self, node_id, port, host="127.0.0.1",
                callback=None, max_connections=0, is_on=False,
                identity=None):
        """ Init function."""
        super().__init__(host, port, node_id, callback, max_connections)
        self.node_id = node_id
        self.port = port
        self.blockchain = []
        self.name = f"nodo{node_id}"
        self.adj = set()
        self.is_on = is_on
        self.identity = identity


    def propagation(self, nodes, data):
        """Function to propagate info."""
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
            elem.propagation(nodes, data)

    def start(self):
        """Start thread."""
        super().start()
        self.is_on = True

    def stop(self):
        """Stop thread."""
        super().stop()
        self.is_on = False

    def get_node_connection(self, node):
        """Get node connection with other node."""
        for elem in self.nodes_outbound:
            if elem.id == node.id:
                return elem
        for elem in self.nodes_inbound:
            if elem.id == node.id:
                return elem
        return None


    def __str__(self):
        """String method."""
        return str(self.to_dict())

    def to_dict(self):
        """Convert in dict."""
        return {"name": self.name, "port": self.port}

    def outbound_node_connected(self, node):
        """outbound_node_connected."""
        print("outbound_node_connected (" + self.id + "): " + node.id)

    def inbound_node_connected(self, node):
        """inbound_node_connected."""
        print("inbound_node_connected: (" + self.id + "): " + node.id)

    def inbound_node_disconnected(self, node):
        """inbound_node_disconnected."""
        print("inbound_node_disconnected: (" + self.id + "): " + node.id)

    def outbound_node_disconnected(self, node):
        """outbound_node_disconnected."""
        print("outbound_node_disconnected: (" + self.id + "): " + node.id)

    def node_message(self, node, data):
        """Def of node message."""
        click.echo(f"Se envió un mensaje desde {node.name}")

    def node_disconnect_with_outbound_node(self, node):
        """node_disconnect_with_outbound_node."""
        print("node wants to disconnect with oher outbound node: (" + self.id + "): " + node.id)

    def node_request_to_stop(self):
        """node_request_to_stop."""
        print("node is requested to stop (" + self.id + "): ")
