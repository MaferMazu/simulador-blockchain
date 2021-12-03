genIdenti -i 5 -n 5
nodo -n nodo1 -d logs -f examples/file_examples/network_file -c examples/file_examples/node_config.txt
nodo -n nodo2
nodo -n nodo3
genTransac -n examples/file_examples/node_file.txt -f examples/file_examples/transac_config.txt -c 1
nodo -n nodo1 -s
nodo -n nodo2 -s
nodo -n nodo3 -s
