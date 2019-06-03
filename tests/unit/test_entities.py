from dataclasses import asdict

from bankrobber.core.entities import BankAccount


def test_bankaccount(account_entity, get_account_response):
    assert asdict(account_entity) == asdict(BankAccount.from_dict(get_account_response))
