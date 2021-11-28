"""Class Network."""

class Network:
    """Class Network."""

    def __init__(self, identities: Identities=Identities()):
        """Init."""
        self.nodes = []
        self.identities = identities
        self.node_config = {"max_block_size": 512, "avgtime": 1, "difficulty": 1000}


    def __str__(self):
        """String method."""
        return str(self.to_dict())


    def to_dict(self):
        """To dict method."""
        return {
            "nodes": [node.to_dict() for node in self.nodes],
            "identities": [str(identity) for identity in self.identities.identities],
            }


    def read_network_file(self):
        """Read Network file."""
        # if node1 and node2:
        #     node1.adj.add(node2)
        #     node2.adj.add(node1)


    def gen_x_nodes(self, num):
        """Return a list of objects."""
        for i in range(1,num+1):
            node = Node(i)
            self.nodes.append(node)
            email = f"{node.name}@example.com"
            self.identities.gen_identity(node.name, email)

