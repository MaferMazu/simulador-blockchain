"""Commands to generate identities, nodes and transactions."""

import click
from models.network import Network

from models.common import import_data, export_data


@click.command(name="genTransac")
@click.option("-d","direc", default="examples/file_examples", type=str, help="directorio de logs")
@click.option("-n","node", default="examples/node_file.txt", type=str, help="archivo con nodos que crean transacciones")
@click.option("-f","file", default="examples/transac_config.txt", type=str, help="archivo de configuracion")
@click.option("-c","count", default=3, type=int, help="cuantas transacciones generar")
def gen_transac(node, direc, file, count):
    """Generate transactions."""
    click.echo("genTransac")
    network = import_data("network")
    if file:
        network.transactions.read_transaction_config(file)
        click.echo(">> Se ha cargado el archivo de configuración.")
    if direc:
        network.directory = direc
        click.echo(f">> Se ha asignado {direc} como directorio de logs.")
    if node:
        network.read_node_file_for_transactions(node)
        click.echo(">> Se ha cargado el archivo de nodos.")

    network.gen_random_transactions(network.identities,count)


@click.command(name="genIdenti")
@click.option("-i","identities", default=3, type=int, help="numero de identidades a generar")
@click.option("-n","nodes", default=3, type=int, help="numero de nodos a generar")
def gen_identi(identities, nodes):
    """Generate identities and nodes."""
    # import pudb; pu.db
    network = Network()
    network.identities.gen_x_identities(identities)
    network.identities.gen_x_nodes(nodes)
    export_data("network", network)
    click.echo(f">> {identities} identidades y {nodes} nodos fueron generados.")
