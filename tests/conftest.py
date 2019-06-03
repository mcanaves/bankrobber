import pytest

from bankrobber.core.entities import BankAccount


@pytest.fixture
def get_account_response():
    return {
        "iban": "iban",
        "currency": "EUR",
        "availableBalance": "0.00",
        "other": "other",
    }


@pytest.fixture
def account_entity():
    return BankAccount(**{"iban": "iban", "currency": "EUR", "balance": "0.00"})
