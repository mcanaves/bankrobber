from typing import Dict, Optional

import requests

from bankrobber.core.clients import BankClient
from bankrobber.core.entities import BankAccount
from config import config


class N26(BankClient):
    def __init__(self):
        self.auth_token = None
        self.refresh_token = None

    def _api_request(self, url, payload: Optional[Dict] = None):
        # TODO: Catch API errors
        # TODO: Catch token expiration case. {'error': 'invalid_token', ...} and
        # reply request with new fresh token.

        if not self.auth_token:
            # TODO: Custom domain exception
            raise Exception("Authentication required. Call `auth` method first.")

        headers = {"Authorization": "bearer " + self.auth_token}
        response = requests.get(
            config["N26"]["api_base_url"] + url, params=payload, headers=headers
        )

        response.raise_for_status()
        return response.json()

    def auth(self, bank_credentials: Dict):
        # TODO: Catch auth errors.
        # - 401 - unauthorized
        # - 400 - {'error': 'invalid_grant', 'error_description': 'Bad credentials'}
        url = config["N26"]["api_base_url"] + "/oauth/token"
        headers = {
            "Authorization": config["N26"]["api_base_auth"],
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        }
        payload = {"grant_type": "password", **bank_credentials}
        response = requests.post(url=url, data=payload, headers=headers)
        response_data = response.json()
        response.raise_for_status()
        self.auth_token = response_data["access_token"]
        self.refresh_token = response_data["refresh_token"]

    def get_account(self) -> BankAccount:
        """Retrieves bank account info."""
        return BankAccount.from_dict(self._api_request("/api/accounts"))
