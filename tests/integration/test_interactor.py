from dataclasses import asdict

from bankrobber.clients.n26 import N26
from bankrobber.core.interactors import BankAccountInformation


def test_bank_account_information(account_entity, get_account_response, mocker):
    credentials = {"username": "username", "password": "secret"}

    mock_post = mocker.patch("bankrobber.clients.n26.requests.post")
    mock_post.return_value.json.return_value = {
        "access_token": "token",
        "refresh_token": "refresh",
    }
    mock_get = mocker.patch("bankrobber.clients.n26.requests.get")
    mock_get.return_value.json.return_value = get_account_response

    assert BankAccountInformation(N26()).execute(credentials) == asdict(account_entity)
