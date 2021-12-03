"""Node command."""

import click

from models.common import import_data, export_data


@click.command(name="node")
@click.option("-n","name", default="nodo1", type=str, help="nombre de nodo a invocar")
@click.option("-d","direc", default="examples/file_examples", type=str, help="directorio de logs")
@click.option("-f","file", default=None, type=str, help="archivo con info de la red")
@click.option("-c","config", default=None, type=str, help="archivo de configuracion de los nodos")
@click.option("-s","stop", is_flag=True, default=False)
def node(name, direc, file, config, stop):
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
        click.echo(f">> Se ha asignado {direc} como directorio de logs.")
    if name:
        node_to_activate = network.search_node_by_name(name)
        if node_to_activate:
            if stop:
                node_to_activate.stop()
            else:
                try:
                    node_to_activate.start()
                    click.echo(f">> Se ha inicializado el {name}.")
                except ConnectionError as error:
                    node_to_activate.is_on = False
                    click.echo(f">> No se inicializó el nodo por el error:\n{error}.")
    export_data("network", network)
