import pytest

from bankrobber.clients.n26 import N26


def test_api_request(mocker):
    mocker.patch.dict("bankrobber.clients.n26.config", {"N26": {"api_base_url": "url"}})
    mock_get = mocker.patch("bankrobber.clients.n26.requests.get")
    mock_get.return_value.json.return_value = {"result": "data"}
    client = N26()
    client.auth_token = "token"
    assert client._api_request(url="/test") == {"result": "data"}
    mock_get.assert_called_once_with(
        "url/test", **{"headers": {"Authorization": "bearer token"}, "params": None}
    )


def test_api_request_without_token():
    with pytest.raises(Exception):
        N26()._api_request(url="/test")


def test_auth(mocker):
    mocker.patch.dict(
        "bankrobber.clients.n26.config",
        {"N26": {"api_base_url": "url", "api_base_auth": "auth"}},
    )
    mock_post = mocker.patch("bankrobber.clients.n26.requests.post")
    mock_post.return_value.json.return_value = {
        "access_token": "token",
        "refresh_token": "refresh",
    }
    client = N26()
    client.auth({"username": "user", "password": "secret"})
    assert client.auth_token == "token"
    assert client.refresh_token == "refresh"
    mock_post.assert_called_once_with(
        **{
            "data": {
                "grant_type": "password",
                "password": "secret",
                "username": "user",
            },
            "headers": {
                "Authorization": "auth",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            },
            "url": "url/oauth/token",
        }
    )


def test_get_account(account_entity, get_account_response, mocker):
    mocker.patch(
        "bankrobber.clients.n26.N26._api_request", return_value=get_account_response
    )
    client = N26()
    assert client.get_account() == account_entity
