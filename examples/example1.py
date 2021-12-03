from models.network import Network


network = Network()
network.identities.gen_x_identities(5)
network.identities.gen_x_nodes(5)
# import pudb; pu.db
network.read_network_file("examples/file_examples/other_network_file.txt")
nodo1 = network.search_node_by_name("nodo1")
nodo2 = network.search_node_by_name("nodo2")
nodo3 = network.search_node_by_name("nodo3")
nodo1.start()
nodo2.start()
nodo3.start()
nodo2.connect_with_node(nodo1.host, int(nodo1.port))
nodo3.connect_with_node(nodo1.host, int(nodo1.port))

network.read_node_file_for_transactions("examples/file_examples/other_node_file.txt")

network.propagation(nodo2, "hola")

nodo1.stop()
nodo2.stop()
nodo3.stop()