from dataclasses import asdict

from bankrobber.core.interactors import BankAccountInformation


def test_bank_account_information(account_entity, mocker):
    credentials = {"username": "username", "password": "secret"}
    mock_client = mocker.patch("bankrobber.core.interactors.BankClient")
    mock_client.get_account.return_value = account_entity
    assert BankAccountInformation(mock_client).execute(credentials) == asdict(
        account_entity
    )
