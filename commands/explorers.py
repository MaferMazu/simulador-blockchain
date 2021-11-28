"""Docstring."""

import click


@click.command(name="explorerBlock")
def explorer_block():
    """Docs."""
    click.echo("explorerBlock")


@click.command(name="explorerTransac")
def explorer_transac():
    """Docs."""
    click.echo("explorerTransac")
