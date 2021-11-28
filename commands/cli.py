"""Docstring."""

import click

from commands.explorers import explorer_block, explorer_transac
from commands.generators import gen_identi, gen_transac
from commands.node import node


def main() -> None:
    """Hold all the commands in a group."""
    cli()


@click.group(context_settings={"help_option_names": ["-h", "--help", "help"]})
def cli() -> None:
    """Define the main group."""


if __name__ == "__main__":
    main()

cli.add_command(node)
cli.add_command(explorer_block)
cli.add_command(explorer_transac)
cli.add_command(gen_identi)
cli.add_command(gen_transac)
