"""
Functions that encapsulate business logic for the app.

Interactor are the place where we implement classes that query the repository,
call the external resources, ... and  apply the business rules, logic, and whatever
transformation we need for our data and return the results.
"""
from dataclasses import asdict
from typing import Dict

from bankrobber.core.clients import BankClient

# TODO: Create base class for all interactor and error layer to catch all interactors
# errors and pass to presentation layer with correct format/error info.


class BankAccountInformation:
    """Retrieves bank account info."""

    def __init__(self, bank_client: BankClient):
        self.bank_client = bank_client

    def execute(self, bank_credentials: Dict) -> Dict:
        self.bank_client.auth(bank_credentials)
        return asdict(self.bank_client.get_account())
