"""Docstring."""

import click
from models.network import Network

from models.common import import_data, export_data


@click.command(name="node")
@click.option("-n","name", default="nodo1", type=str, help="nombre de nodo a invocar")
@click.option("-d","dir", default="file_examples", type=str, help="directorio de logs")
@click.option("-f","file", default=None, type=str, help="archivo con info de la red")
@click.option("-c","config", default=None, type=str, help="archivo de configuracion de los nodos")
def node():
    """Docs."""
    click.echo("Node")
    object_name = "network"
    network = import_data(object_name)
    print(network)
