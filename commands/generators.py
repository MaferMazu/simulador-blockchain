"""Commands to generate identities, nodes and transactions."""

import click
from models.network import Network

from models.common import import_data, export_data


@click.command(name="genTransac")
def gen_transac():
    """Docs."""
    click.echo("genTransac")


@click.command(name="genIdenti")
@click.option("-i","identities", default=3, type=int, help="numero de identidades a generar")
@click.option("-n","nodes", default=3, type=int, help="numero de nodos a generar")
def gen_identi(identities, nodes):
    """Generate identities and nodes."""

    network = Network()
    network.identities.gen_x_identities(identities)
    network.gen_x_nodes(nodes)
    export_data("network", network)
    click.echo(f">> {identities} identidades y {nodes} nodos fueron generados.")
