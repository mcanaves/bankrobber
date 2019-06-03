import click

from bankrobber.clients.n26 import N26
from bankrobber.core.interactors import BankAccountInformation


@click.group()
def n26():
    """
    App to interact with banks from terminal. As this app is for demo purpose
    only works with N26 bank for now.
    """


@n26.command()
@click.argument("username")
@click.argument("password")
def get_account(username: str, password: str):
    """ Get bank account information."""
    # TODO: read username and password from input instead of command argument
    # to avoid credentials been saved in terminal historial
    use_case = BankAccountInformation(N26())
    print(use_case.execute({"username": username, "password": password}))


if __name__ == "__main__":  # pragma: nocover
    n26()
