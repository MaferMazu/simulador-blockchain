"""Node command."""

import click
from models.network import Network

from models.common import import_data, export_data


@click.command(name="node")
@click.option("-n","name", default="nodo1", type=str, help="nombre de nodo a invocar")
@click.option("-d","direc", default="file_examples", type=str, help="directorio de logs")
@click.option("-f","file", default=None, type=str, help="archivo con info de la red")
@click.option("-c","config", default=None, type=str, help="archivo de configuracion de los nodos")
def node():
    """Exec node."""
    network = import_data("network")

    if config:
        network.read_node_config(config)
        click.echo(">> Se ha cargado el archivo de configuracion.")
    if file:
        network.read_network_file(file)
        click.echo(">> Se ha cargado el archivo de red.")
    if direc:
        network.directory = direc
        click.echo(f">> Se ha asignado {dir} como directorio de logs.")
    if name:
        node = network.search_node_by_name(name)
        if node:
            try:
                node.is_on = True
                node.start()
                click.echo(f">> Se ha inicializado el {name}.")
            except Exception as e:
                node.is_on = False
                click.echo(f">> No se inicializó el nodo por el error:\n{e}.")
    export_data("network", network)
