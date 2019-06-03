"""
Contracts that acts as boundary between app core and data providers layer.
"""
from typing import Dict

from bankrobber.core.entities import BankAccount


class BankClient:
    def auth(self, bank_credentials: Dict):
        raise NotImplementedError

    def get_account(self) -> BankAccount:
        raise NotImplementedError
