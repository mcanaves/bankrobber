from dataclasses import asdict

from click.testing import CliRunner

from bankrobber.cli import get_account


def test_get_account(account_entity, mocker):
    mocker.patch(
        "bankrobber.cli.BankAccountInformation.execute",
        return_value=asdict(account_entity),
    )
    runner = CliRunner()
    result = runner.invoke(get_account, ["username", "secret"])
    assert result.exit_code == 0
    assert result.output == "{'iban': 'iban', 'currency': 'EUR', 'balance': '0.00'}\n"
